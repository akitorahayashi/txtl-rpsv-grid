## Overview

A Textual app template with a responsive grid button view.

<img width="598" height="391" alt="スクリーンショット" src="https://github.com/user-attachments/assets/76b4c704-bbac-4caa-940d-0ebf5e414c75" />

## Setup and Execution

1.  **Initial Setup**

    Run the setup command to install dependencies and create the `.env` file from the example.

    ```bash
    make setup
    ```

2.  **Environment Configuration**

    Modify the `.env` file with your local configuration, such as the host ip and ports.

3.  **Launch Application**

    Start the Textual application using the development server.

    ```bash
    make run
    ```

## Development Workflow

-   **Code Formatting**

    To automatically format the code, run:

    ```bash
    make format
    ```

-   **Linter Execution**

    To check the code for linting issues, run:

    ```bash
    make lint
    ```

-   **Testing**

    To run the entire test suite (ui, e2e), use:

    ```bash
    make test
    ```

    You can also run specific test suites:

    ```bash
    make ui-test
    make e2e-test
    ```
