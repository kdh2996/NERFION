# Copyright 2004-2015 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import renpy.display
import time
import collections

import datetime

# Profiling ####################################################################

profile_log = renpy.log.open("profile_screen", developer=True, append=False, flush=False)

# A map from screen name to ScreenProfile object.
profile = { }

class ScreenProfile(renpy.object.Object):
    """
    :doc: profile_screen
    :name: renpy.profile_screen

    """

    def __init__(self, name, predict=False, show=False, update=False, request=False, time=False, debug=False, const=False):
        """
        Requests screen profiling for the screen named `name`, which
        must be a string.

        Apart from `name`, all arguments must be supplied as keyword
        arguments. This function takes three groups of arguments.


        The first group of arguments determines when profiling occurs.

        `predict`
            If true, profiling occurs when the screen is being predicted.

        `show`
            If true, profiling occurs when the screen is first shown.

        `update`
            If true, profiling occurs when the screen is updated.

        `request`
            If true, profiling occurs when requested by pressing F8.

        The second group of arguments controls what profiling output is
        produced when profiling occurs.

        `time`
            If true, Ren'Py will log the amount of time it takes to evaluate
            the screen.

        `debug`
            If true, Ren'Py will log information as to how screens are
            evaluated, including:

            * Which displayables Ren'Py considers constant.
            * Which arguments, if any, needed to be evaluated.
            * Which displayables were reused.

            Producing and saving this debug information takes a noticeable
            amount of time, and so the `time` output should not be considered
            reliable if `debug` is set.

        The last group of arguments controls what output is produced once
        per Ren'Py run.

        `const`
            Displays the variables in the screen that are marked as const and
            not-const.

        All profiling profiling output will be logged to profile_screen.txt in
        the game directory.
        """

        self.predict = predict
        self.show = show
        self.update = update
        self.request = request

        self.time = time
        self.debug = debug

        self.const = const

        if name is not None:
            if isinstance(name, basestring):
                name = tuple(name.split())
                profile[name] = self

def get_profile(name):
    """
    Returns the profile object for the screen with `name`, or a default
    profile object if none exists.

    `name`
        A string or tuple.
    """

    if isinstance(name, basestring):
        name = tuple(name.split())

    if name in profile:
        return profile[name]
    else:
        return ScreenProfile(None)

# Cache ########################################################################

# A map from screen name to a list of ScreenCache objects. We ensure the cache
# does not exceed config.screen_cache_size for each screen.
predict_cache = collections.defaultdict(list)

class ScreenCache(object):
    """
    Represents an entry in the screen cache. Upon creation, puts itself into
    the screen cache.
    """

    def __init__(self, screen, args, kwargs, cache):

        if screen.ast is None:
            return

        self.args = args
        self.kwargs = kwargs
        self.cache = cache

        pc = predict_cache[screen]

        pc.append(self)

        if len(pc) > renpy.config.screen_cache_size:
            pc.pop(0)

cache_put = ScreenCache

def cache_get(screen, args, kwargs):
    """
    Returns the cache to use when `screen` is accessed with `args` and
    `kwargs`.
    """

    if screen.ast is None:
        return { }

    pc = predict_cache[screen]

    if not pc:
        return { }

    for sc in pc:

        # Reuse w/ same arguments.
        if sc.args == args and sc.args == kwargs:
            pc.remove(sc)
            break
    else:

        # Reuse the oldest.
        sc = pc.pop(0)

    return sc.cache


# Screens #####################################################################




class Screen(renpy.object.Object):
    """
    A screen is a collection of widgets that are displayed together.
    This class stores information about the screen.
    """

    def __init__(self,
                 name,
                 function,
                 modal="False",
                 zorder="0",
                 tag=None,
                 predict=None,
                 variant=None,
                 parameters=False,
                 location=None):

        # The name of this screen.
        if isinstance(name, basestring):
            name = tuple(name.split())

        self.name = name

        screens[name[0], variant] = self

        # A function that can be called to display the screen.
        self.function = function

        # If this is a SL2 screen, the SLScreen node at the root of this
        # screen.
        if isinstance(function, renpy.sl2.slast.SLScreen): # @UndefinedVariable
            self.ast = function
        else:
            self.ast = None

        # Expression: Are we modal? (A modal screen ignores screens under it.)
        self.modal = modal

        # Expression: Our zorder.
        self.zorder = zorder

        # The tag associated with the screen.
        self.tag = tag or name[0]

        # Can this screen be predicted?
        if predict is None:
            predict = renpy.config.predict_screens

        self.predict = predict

        # True if this screen takes parameters via _args and _kwargs.
        self.parameters = parameters

        # The location (filename, linenumber) of this screen.
        self.location = location


# Phases we can be in.
PREDICT = 0 # Predicting the screen before it is shown.
SHOW = 1    # Showing the screen for the first time.
UPDATE = 2  # Showing the screen for the second and later times.
HIDE = 3    # After the screen has been hid with "hide screen" (or the end of call screen).
OLD = 4     # A copy of the screen in the old side of a transition.

phase_name = [
    "PREDICT",
    "SHOW",
    "UPDATE",
    "HIDE",
    "OLD",
    ]

class ScreenDisplayable(renpy.display.layout.Container):
    """
    A screen is a collection of widgets that are displayed together. This
    class is responsible for managing the display of a screen.
    """

    nosave = [ 'screen', 'child', 'children', 'transforms', 'widgets', 'old_widgets', 'hidden_widgets', 'old_transforms', 'cache', 'profile', 'phase', 'use_cache' ]

    restarting = False
    hiding = False

    def after_setstate(self):
        self.screen = get_screen_variant(self.screen_name[0])
        self.child = None
        self.children = [ ]
        self.transforms = { }
        self.widgets = { }
        self.old_widgets = None
        self.old_transforms = None
        self.hidden_widgets = { }
        self.cache = { }
        self.phase = UPDATE
        self.use_cache = { }

        self.profile = profile.get(self.screen_name, None)

    def __init__(self, screen, tag, layer, widget_properties={}, scope={}, **properties):

        super(ScreenDisplayable, self).__init__(**properties)

        # Stash the properties, so we can re-create the screen.
        self.properties = properties

        # The screen, and it's name. (The name is used to look up the
        # screen on save.)
        self.screen = screen
        self.screen_name = screen.name

        self._location = self.screen.location

        # The profile object that determines when we profile.
        self.profile = profile.get(self.screen_name, None)

        # The tag and layer screen was displayed with.
        self.tag = tag
        self.layer = layer

        # The scope associated with this statement. This is passed in
        # as keyword arguments to the displayable.
        self.scope = renpy.python.RevertableDict(scope)

        # The child associated with this screen.
        self.child = None

        # Widget properties given to this screen the last time it was
        # shown.
        self.widget_properties = widget_properties

        # A map from name to the widget with that name.
        self.widgets = { }

        # The persistent cache.
        self.cache = { }

        if tag and layer:
            old_screen = get_screen(tag, layer)
        else:
            old_screen = None

        # A map from name to the transform with that name. (This is
        # taken from the old version of the screen, if it exists.
        if old_screen is not None:
            self.transforms = old_screen.transforms
        else:
            self.transforms = { }

        # A map from a (screen name, id) pair to cache. This is for use
        # statements with the id parameter.
        if old_screen is not None:
            self.use_cache = old_screen.use_cache
        else:
            self.use_cache = { }


        # What widgets and transforms were the last time this screen was
        # updated. Used to communicate with the ui module, and only
        # valid during an update - not used at other times.
        self.old_widgets = None
        self.old_transforms = None

        # Should we transfer data from the old_screen? This becomes
        # true once this screen finishes updating for the first time,
        # and also while we're using something.
        self.old_transfers = (old_screen and old_screen.screen_name == self.screen_name)

        # The current transform event, and the last transform event to
        # be processed.
        self.current_transform_event = None

        # A dict-set of widgets (by id) that have been hidden from us.
        self.hidden_widgets = { }

        # Are we restarting or hiding?
        self.restarting = False
        self.hiding = False

        # Modal and zorder.
        self.modal = renpy.python.py_eval(self.screen.modal, locals=self.scope)
        self.zorder = renpy.python.py_eval(self.screen.zorder, locals=self.scope)

        # The lifecycle phase we are in - one of PREDICT, SHOW, UPDATE, or HIDE.
        self.phase = PREDICT

    def __unicode__(self):
        return "Screen {}".format(" ".join(self.screen_name))

    def visit(self):
        return [ self.child ]

    def visit_all(self, callback):
        callback(self)

        try:
            push_current_screen(self)
            self.child.visit_all(callback)
        finally:
            pop_current_screen()

    def per_interact(self):
        renpy.display.render.redraw(self, 0)
        self.update()

    def set_transform_event(self, event):
        super(ScreenDisplayable, self).set_transform_event(event)
        self.current_transform_event = event

    def find_focusable(self, callback, focus_name):

        hiding = (self.phase == OLD) or (self.phase == HIDE)

        try:
            push_current_screen(self)

            if self.child and not hiding:
                self.child.find_focusable(callback, focus_name)
        finally:
            pop_current_screen()

    def copy(self):
        rv = ScreenDisplayable(self.screen, self.tag, self.layer, self.widget_properties, self.scope, **self.properties)
        rv.transforms = self.transforms.copy()
        rv.widgets = self.widgets.copy()
        rv.old_transfers = True
        rv.child = self.child

        return rv

    def _hide(self, st, at, kind):

        if self.phase == HIDE:
            hid = self
        else:

            updated_screens.discard(self)
            self.update()

            if self.screen is None:
                return None

            if self.child is None:
                return None

            if self.screen.ast is not None:
                self.screen.ast.copy_on_change(self.cache.get(0, {}))

            hid = self.copy()

            for i in self.child.children:
                i.set_transform_event(kind)

        hid.phase = HIDE

        rv = None

        old_child = hid.child

        if not isinstance(old_child, renpy.display.layout.MultiBox):
            return None

        renpy.ui.detached()
        hid.child = renpy.ui.fixed(focus="_screen_" + "_".join(self.screen_name))
        hid.children = [ hid.child ]
        renpy.ui.close()

        for d in old_child.children:
            c = d._hide(st, at, kind)

            if c is not None:
                renpy.display.render.redraw(c, 0)
                hid.child.add(c)

                rv = hid

        if hid is not None:
            renpy.display.render.redraw(hid, 0)

        return rv

    def _in_old_scene(self):

        if self.screen is None:
            return self

        if self.child is None:
            return self

        if not renpy.config.transition_screens:
            return self

        if self.screen.ast is not None:
            self.screen.ast.copy_on_change(self.cache.get(0, {}))

        rv = self.copy()
        rv.phase = OLD
        return rv


    def update(self):

        if self in updated_screens:
            return

        updated_screens.add(self)

        if self.screen is None:
            self.child = renpy.display.layout.Null()
            return { }

        # Do not update if restarting or hiding.
        if self.restarting or (self.phase == HIDE) or (self.phase == OLD):
            if not self.child:
                self.child = renpy.display.layout.Null()

            return self.widgets

        profile = False
        debug = False

        if self.profile:

            if self.phase == UPDATE and self.profile.update:
                profile = True
            elif self.phase == SHOW and self.profile.show:
                profile = True
            elif self.phase == PREDICT and self.profile.predict:
                profile = True

            if renpy.display.interface.profile_once and self.profile.request:
                profile = True

            if profile:
                profile_log.write("%s %s %s",
                    phase_name[self.phase],
                    " ".join(self.screen_name),
                    datetime.datetime.now().strftime("%H:%M:%S.%f"))

                start = time.time()

                if self.profile.debug:
                    debug = True


        # Cycle widgets and transforms.
        self.old_widgets = self.widgets
        self.old_transforms = self.transforms
        self.widgets = { }
        self.transforms = { }

        push_current_screen(self)

        old_ui_screen = renpy.ui.screen
        renpy.ui.screen = self

        # Evaluate the screen.
        try:

            renpy.ui.detached()
            self.child = renpy.ui.fixed(focus="_screen_" + "_".join(self.screen_name))
            self.children = [ self.child ]

            self.scope["_scope"] = self.scope
            self.scope["_name"] = 0
            self.scope["_debug"] = debug

            self.screen.function(**self.scope)

            renpy.ui.close()

        finally:
            renpy.ui.screen = old_ui_screen
            pop_current_screen()

        # Finish up.
        self.old_widgets = None
        self.old_transforms = None
        self.old_transfers = True

        if self.current_transform_event:

            for i in self.child.children:
                i.set_transform_event(self.current_transform_event)

            self.current_transform_event = None

        if profile:
            end = time.time()

            if self.profile.time:
                profile_log.write("* %.2f ms", 1000 * (end - start))

            if self.profile.debug:
                profile_log.write("\n")

        if self.phase == SHOW:
            self.phase = UPDATE

        return self.widgets

    def render(self, w, h, st, at):

        if not self.child:
            self.update()

        try:
            push_current_screen(self)
            child = renpy.display.render.render(self.child, w, h, st, at)
        finally:
            pop_current_screen()

        rv = renpy.display.render.Render(w, h)
        rv.focus_screen = self

        hiding = (self.phase == OLD) or (self.phase == HIDE)

        rv.blit(child, (0, 0), focus=not hiding, main=not hiding)
        rv.modal = self.modal and not hiding

        return rv

    def get_placement(self):
        if not self.child:
            self.update()

        return self.child.get_placement()

    def event(self, ev, x, y, st):

        if (self.phase == OLD) or (self.phase == HIDE):
            return

        try:
            push_current_screen(self)

            rv = self.child.event(ev, x, y, st)
        finally:
            pop_current_screen()

        if rv is not None:
            return rv

        if self.modal:
            raise renpy.display.layout.IgnoreLayers()

    def get_phase_name(self):
        return phase_name[self.phase]

# The name of the screen that is currently being displayed, or
# None if no screen is being currently displayed.
_current_screen = None

# The stack of old current screens.
current_screen_stack = [ ]

def push_current_screen(screen):
    global _current_screen
    current_screen_stack.append(_current_screen)
    _current_screen = screen

def pop_current_screen():
    _current_screen = current_screen_stack.pop()

# A map from (screen_name, variant) tuples to screen.
screens = { }

# The screens that were updated during the current interaction.
updated_screens = set()

def get_screen_variant(name):
    """
    Get a variant screen object for `name`.
    """

    for i in renpy.config.variants:
        rv = screens.get((name, i), None)
        if rv is not None:
            return rv

    return None


prepared = False

def prepare_screens():
    """
    Prepares all screens for use.
    """

    global prepared

    if prepared:
        return

    predict_cache.clear()

    for s in screens.values():
        if s.ast is None:
            continue

        s.ast.unprepare()

    for s in screens.values():
        if s.ast is None:
            continue

        s.ast.prepare()

    prepared = True

def define_screen(*args, **kwargs):
    """
    :doc: screens
    :args: (name, function, modal="False", zorder="0", tag=None, variant=None)

    Defines a screen with `name`, which should be a string.

    `function`
        The function that is called to display the screen. The
        function is called with the screen scope as keyword
        arguments. It should ignore additional keyword arguments.

        The function should call the ui functions to add things to the
        screen.

    `modal`
        A string that, when evaluated, determines of the created
        screen should be modal. A modal screen prevents screens
        underneath it from receiving input events.

    `zorder`
        A string that, when evaluated, should be an integer. The integer
        controls the order in which screens are displayed. A screen
        with a greater zorder number is displayed above screens with a
        lesser zorder number.

    `tag`
        The tag associated with this screen. When the screen is shown,
        it replaces any other screen with the same tag. The tag
        defaults to the name of the screen.

    `predict`
        If true, this screen can be loaded for image prediction. If false,
        it can't. Defaults to true.

    `variant`
        String. Gives the variant of the screen to use.

    """

    Screen(*args, **kwargs)


def get_screen(name, layer="screens"):
    """
    :doc: screens

    Returns the ScreenDisplayable with the given `tag`, on
    `layer`. If no displayable with the tag is not found, it is
    interpreted as screen name. If it's still not found, None is returned.
     """

    if isinstance(name, basestring):
        name = tuple(name.split())

    tag = name[0]

    sl = renpy.exports.scene_lists()

    sd = sl.get_displayable_by_tag(layer, tag)

    if sd is None:
        sd = sl.get_displayable_by_name(layer, name)

    return sd


def has_screen(name):
    """
    Returns true if a screen with the given name exists.
    """

    if not isinstance(name, tuple):
        name = tuple(name.split())

    if not name:
        return False

    if get_screen_variant(name[0]):
        return True
    else:
        return False

def show_screen(_screen_name, *_args, **kwargs):
    """
    :doc: screens

    The programmatic equivalent of the show screen statement.

    Shows the named screen. This takes the following keyword arguments:

    `_screen_name`
        The name of the  screen to show.
    `_layer`
        The layer to show the screen on.
    `_tag`
        The tag to show the screen with. If not specified, defaults to
        the tag associated with the screen. It that's not specified,
        defaults to the name of the screen.,
    `_widget_properties`
        A map from the id of a widget to a property name -> property
        value map. When a widget with that id is shown by the screen,
        the specified properties are added to it.
    `_transient`
        If true, the screen will be automatically hidden at the end of
        the current interaction.

    Keyword arguments not beginning with underscore (_) are used to
    initialize the screen's scope.
    """

    _layer = kwargs.pop("_layer", "screens")
    _tag = kwargs.pop("_tag", None)
    _widget_properties = kwargs.pop("_widget_properties", {})
    _transient = kwargs.pop("_transient", False)

    name = _screen_name

    if not isinstance(name, tuple):
        name = tuple(name.split())

    screen = get_screen_variant(name[0])

    if screen is None:
        raise Exception("Screen %s is not known.\n" % (name[0],))

    if _tag is None:
        _tag = screen.tag

    scope = { }

    if screen.parameters:
        scope["_kwargs" ] = kwargs
        scope["_args"] = _args
    else:
        scope.update(kwargs)

    d = ScreenDisplayable(screen, _tag, _layer, _widget_properties, scope)

    old_d = get_screen(name, _layer)

    if old_d and old_d.cache:
        d.cache = old_d.cache
        d.phase = UPDATE
    else:
        d.cache = cache_get(screen, _args, kwargs)
        d.phase = SHOW

    sls = renpy.display.core.scene_lists()

    sls.add(_layer, d, _tag, zorder=d.zorder, transient=_transient, keep_st=True, name=name)


def predict_screen(_screen_name, *_args, **kwargs):
    """
    Predicts the displayables that make up the given screen.

    `_screen_name`
        The name of the  screen to show.
    `_widget_properties`
        A map from the id of a widget to a property name -> property
        value map. When a widget with that id is shown by the screen,
        the specified properties are added to it.

    Keyword arguments not beginning with underscore (_) are used to
    initialize the screen's scope.
    """

    _layer = kwargs.pop("_layer", "screens")
    _tag = kwargs.pop("_tag", None)
    _widget_properties = kwargs.pop("_widget_properties", {})
    _transient = kwargs.pop("_transient", False)

    name = _screen_name

    if renpy.config.debug_image_cache:
        renpy.display.ic_log.write("Predict screen %s", name)

    if not isinstance(name, tuple):
        name = tuple(name.split())

    screen = get_screen_variant(name[0])

    scope = { }
    scope["_scope"] = scope

    if screen.parameters:
        scope["_kwargs" ] = kwargs
        scope["_args"] = _args
    else:
        scope.update(kwargs)

    try:

        if screen is None:
            raise Exception("Screen %s is not known.\n" % (name[0],))

        if not screen.predict:
            return

        d = ScreenDisplayable(screen, None, None, _widget_properties, scope)
        d.cache = cache_get(screen, _args, kwargs)
        d.update()
        cache_put(screen, _args, kwargs, d.cache)

        renpy.display.predict.displayable(d)

    except:
        if renpy.config.debug_image_cache:
            import traceback

            print "While predicting screen", _screen_name
            traceback.print_exc()

    renpy.ui.reset()


def hide_screen(tag, layer='screens'):
    """
    :doc: screens

    The programmatic equivalent of the hide screen statement.

    Hides the screen with `tag` on `layer`.
    """

    screen = get_screen(tag, layer)

    if screen is not None:
        renpy.exports.hide(screen.tag, layer=layer)

def use_screen(_screen_name, *_args, **kwargs):

    _name = kwargs.pop("_name", ())
    _scope = kwargs.pop("_scope", { })

    name = _screen_name

    if not isinstance(name, tuple):
        name = tuple(name.split())

    screen = get_screen_variant(name[0])

    if screen is None:
        raise Exception("Screen %r is not known." % (name,))

    old_transfers = _current_screen.old_transfers
    _current_screen.old_transfers = True

    if screen.parameters:
        scope = { }
        scope["_kwargs"] = kwargs
        scope["_args"] = _args
    else:
        scope = _scope.copy()
        scope.update(kwargs)

    scope["_scope"] = scope
    scope["_name"] = (_name, name)

    screen.function(**scope)

    _current_screen.old_transfers = old_transfers

def current_screen():
    return _current_screen

def get_widget(screen, id, layer='screens'): #@ReservedAssignment
    """
    :doc: screens

    From the `screen` on `layer`, returns the widget with
    `id`. Returns None if the screen doesn't exist, or there is no
    widget with that id on the screen.
    """

    if isinstance(screen, ScreenDisplayable):
        screen = screen.screen_name

    if screen is None:
        screen = current_screen()
    else:
        screen = get_screen(screen, layer)

    if not isinstance(screen, ScreenDisplayable):
        return None

    if screen.child is None:
        screen.update()

    rv = screen.widgets.get(id, None)
    return rv

def before_restart():
    """
    This is called before Ren'Py restarts to put the screens into restart
    mode, which prevents crashes due to variables being used that are no
    longer defined.
    """

    for k, layer in renpy.display.interface.old_scene.iteritems():
        if k is None:
            continue

        for i in layer.children:
            if isinstance(i, ScreenDisplayable):
                i.restarting = True

