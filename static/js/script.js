const HOME_BUTTON = Document.getElementById("home-but")
const HELP_BUTTON = Document.getElementById("help-but")
const COMMAND_BUTTON = Document.getElementById("command-but")

// Command HELP_BUTTOn
COMMAND_BUTTON.addeventListener("click", event => {
    return Window.prompt("Bist du ein Admin?")

})
