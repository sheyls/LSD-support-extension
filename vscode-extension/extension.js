const vscode = require('vscode');
const path = require('path');
const { exec } = require('child_process');

function activate(context) {
    let disposable = vscode.commands.registerCommand('lsystem.compile', function () {

        let compilerRoot = vscode.workspace.getConfiguration('lsd').get('compilerRoot');
        let pythonScriptPath = `${compilerRoot}`; // Assuming this is the relative path from the root to the python script.
        
        if (!compilerRoot) {
            vscode.window.showInputBox({
                prompt: 'Please provide the path to the LSD compiler root directory.',
                placeHolder: '/path/to/compiler/root'
            }).then(inputValue => {
                if (inputValue) {
                    let config = vscode.workspace.getConfiguration('lsd');
                    config.update('compilerRoot', inputValue, vscode.ConfigurationTarget.Global);
                }
            });
        }
        
        // Get the path of the active file in the editor
        let filePath = vscode.window.activeTextEditor.document.fileName;

        // Ensure the file has a .lsystem extension
        if (path.extname(filePath) !== '.lsystem') {
            vscode.window.showErrorMessage('The selected file is not an .lsystem file!');
            return;
        }

        // Invoke the Python compiler
        exec(`python ${pythonScriptPath} ${filePath}`, (error, stdout, stderr) => {
            //if (error) {
              //  vscode.window.showErrorMessage(`Error compiling .lsystem file: ${stderr}`);
                return;
            //}
            // If you have any output to show or if the compilation was successful
            vscode.window.showInformationMessage(stdout);
        });
    });

    context.subscriptions.push(disposable);
}

exports.activate = activate;

function deactivate() {}

exports.deactivate = deactivate;
