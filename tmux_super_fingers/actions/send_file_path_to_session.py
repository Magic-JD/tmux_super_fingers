import os

from .action import Action
from ..targets.target_payload import EditorOpenable
from ..cli_adapter import RealCliAdapter, CliAdapter

# emacs go to line number:
#   send-keys -t %3 M-x goto-line Enter 3 Enter


class SendFilePathToSession(Action):
    def __init__(self, target_payload: EditorOpenable, cli_adapter: CliAdapter = RealCliAdapter()):
        self.target_payload = target_payload
        self.cli_adapter = cli_adapter

    def perform(self) -> None:
        editor_pane = self.cli_adapter.current_tmux_window_panes_props()[0]

        if editor_pane:
            self.cli_adapter.select_tmux_window(editor_pane.pane_id)
            self.cli_adapter.tmux_send_keys(
                editor_pane.pane_id,
                f" 'cd {self.target_payload.file_path}'"
            )
        else:
            print("Failure to find session")
