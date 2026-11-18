#!/usr/bin/env python3
"""PreToolUse 훅: 도구 이름만으로는 삭제인지 알 수 없는 호출을 인자까지 보고 막는다.
- Notion update-page에 allow_deleting_content: true (하위 페이지/DB 삭제 우회)
- Artifact 도구의 action: "delete", claude-artifacts delete_artifact
사용자가 이번 턴에 "삭제 너가해줘"라고 말했을 때(삭제 허용 표시 파일이 있을 때)만 통과한다.
삭제가 아닌 호출은 아무 출력 없이 통과시킨다."""
import json, os, sys

FLAG = os.environ.get("KIMCO_DELETE_FLAG", "/tmp/kimco-delete-allowed")
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

name = data.get("tool_name", "") or ""
args = data.get("tool_input", {}) or {}

reason = None
hint = ""
if name.endswith("notion-update-page") and args.get("allow_deleting_content") is True:
    reason = "Notion 페이지 수정에서 하위 페이지·DB 삭제(allow_deleting_content)를 허용하려 했습니다."
    hint = " 지워질 항목 없이 순서만 바꾸려면 allow_deleting_content 없이 다시 시도하세요."
elif name == "Artifact" and args.get("action") == "delete":
    reason = "아티팩트 삭제를 시도했습니다."
elif name.endswith("delete_artifact"):
    reason = "아티팩트 삭제를 시도했습니다."

if reason is None or os.path.exists(FLAG):
    sys.exit(0)

print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": reason + " 삭제는 사용자가 \"삭제 너가해줘\"라고 직접 말했을 때만 가능합니다." + hint,
}}, ensure_ascii=False))
