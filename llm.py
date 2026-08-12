import litert_lm

litert_lm.set_min_log_severity(litert_lm.LogSeverity.ERROR) # Hide log for TUI app

with litert_lm.Engine("path/to/model.litertlm") as engine:
  with engine.create_conversation() as conversation:
    while True:
      user_input = input("\n>>> ")
      for chunk in conversation.send_message_async(user_input):
        print(chunk["content"][0]["text"], end="", flush=True)