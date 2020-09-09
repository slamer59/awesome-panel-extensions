# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel_extensions.frameworks.fast import FastTextInput
from tests.frameworks.fast.fast_test_app import create_fast_test_app


def test_constructor():
    # When
    textinput = FastTextInput(name="TextInput")
    # Then
    assert textinput.name == "TextInput"
    assert textinput.value == ""
    assert textinput.appearance == "outline"
    assert textinput.autofocus is False
    assert textinput.placeholder == ""
    assert textinput.type_of_text == "text"
    assert textinput.maxlength is None
    assert textinput.minlength is None
    assert textinput.pattern is None
    assert textinput.size is None
    assert textinput.spellcheck is False
    assert textinput.required is False
    assert textinput.disabled is False
    assert textinput.readonly is False


if __name__ == "__main__":
    textinput = FastTextInput(name="Be Fast!", placeholder="Write something!")
    app = create_fast_test_app(
        component=textinput,
        parameters=[
            "name",
            "value",
            "disabled",
            "placeholder",
            "appearance",
            "autofocus",
            "type_of_text",
            # Some attributes do not work. See https://github.com/microsoft/fast/issues/3852
            # "maxlength",
            # "minlength",
            # "pattern",
            # "size",
            # "spellcheck",
            # "required",
            "readonly",
        ],
    )
    app.show(port=5007)