# Intro

# Troubleshooting

If you ran `uv add streamlit` but cannot run the `streamlit` CLI, the most likely cause is that your terminal session is not using the virtual environment where Streamlit was installed. Here’s how to resolve it:

- **Activate the virtual environment:**  
  If you used `uv` to manage dependencies, it typically creates a `.venv` directory. You need to activate it before running the Streamlit CLI:
  - On Windows:  
    ```
    .venv\Scripts\activate
    ```
  - On macOS/Linux:  
    ```
    source .venv/bin/activate
    ```
  After activation, try running:
  ```
  streamlit run your_script.py
  ```
  This should work if Streamlit is installed in the active environment[5][7].

- **Check your PATH:**  
  If you still get a "command not found" error, the `streamlit` executable might not be in your PATH. This can happen if the virtual environment is not activated or if the installation was incomplete[6].

- **Try running as a module:**  
  Alternatively, you can run Streamlit using Python directly:
  ```
  python -m streamlit run your_script.py
  ```
  This ensures you are using the Streamlit installed in your current environment[7].

- **Restart your terminal:**  
  Sometimes, changes to the environment are not picked up until you restart your terminal session[2].

If you follow these steps and still cannot run the CLI, double-check that Streamlit appears in your environment by running:
```
uv pip list
```
If it’s missing, reinstall it with `uv add streamlit` while your virtual environment is activated[5].

In summary: activate your `.venv` before running `streamlit`, and use `python -m streamlit` as a fallback if needed.

Sources
[1] Install Streamlit using command line https://docs.streamlit.io/get-started/installation/command-line
[2] ModuleNotFoundError: No module named 'streamlit.cli' https://stackoverflow.com/questions/68162180/modulenotfounderror-no-module-named-streamlit-cli/72076104
[3] No module named 'streamlit.cli' - python - Stack Overflow https://stackoverflow.com/questions/73514548/no-module-named-streamlit-cli
[4] Cannot import name 'cli' from 'streamlit' https://discuss.streamlit.io/t/cannot-import-name-cli-from-streamlit/30093
[5] data-sloth/uv-streamlit-setup: A template repo with uv ... - GitHub https://github.com/data-sloth/uv-streamlit-setup/
[6] Command not found - Using Streamlit https://discuss.streamlit.io/t/command-not-found/741
[7] Run your Streamlit app https://docs.streamlit.io/develop/concepts/architecture/run-your-app
[8] python streamlit run issue - Stack Overflow https://stackoverflow.com/questions/60866205/python-streamlit-run-issue
[9] Help troubleshooting "command not found error" with streamlit app https://www.reddit.com/r/docker/comments/1hk3j23/help_troubleshooting_command_not_found_error_with/
[10] Error installing requirements on streamlit cloud https://discuss.streamlit.io/t/error-installing-requirements-on-streamlit-cloud/84631
[11] How to use uvicorn and streamlit in a UV environment? · Issue #12267 https://github.com/astral-sh/uv/issues/12267
[12] Allow streamlit app to be run as a normal python script with ... - GitHub https://github.com/streamlit/streamlit/issues/9450
[13] Oh no error! - Community Cloud - Streamlit https://discuss.streamlit.io/t/oh-no-error/68696
[14] ModuleNotFoundError: No module named 'streamlit' https://discuss.streamlit.io/t/modulenotfounderror-no-module-named-streamlit/73313
[15] Fanilo Andrianasolo on X: "Installing UV and running Streamlit in a ... https://x.com/andfanilo/status/1826914086652657666
[16] Install Streamlit https://docs.streamlit.io/get-started/installation
[17] How to create a Streamlit app in VS Code - YouTube https://www.youtube.com/watch?v=O3oPpSYIkm4
