#!/usr/bin/env python3
"""UserPromptSubmit 훅: 사용자가 '삭제 너가해줘'라고 말한 턴에만 삭제 허용 표시를 만든다.
다른 모든 메시지에서는 표시를 지워 삭제가 다시 잠기게 한다."""
import json, os, re, sys

FLAG = os.environ.get("KIMCO_DELETE_FLAG", "/tmp/kimco-delete-allowed")
try:
    prompt = json.load(sys.stdin).get("prompt", "") or ""
except Exception:
    prompt = ""

allowed = bool(re.search(r"삭제", prompt) and re.search(r"(너가|네가|니가|너 ?가)\s*해\s*줘|해\s*줘", prompt) and re.search(r"(너가|네가|니가)\s*해\s*줘", prompt))
if allowed:
    open(FLAG, "w").write("1")
else:
    try:
        os.remove(FLAG)
    except FileNotFoundError:
        pass
