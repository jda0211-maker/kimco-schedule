#!/usr/bin/env bash
# 삭제 계열 도구 호출 게이트.
# 사용자가 이번 턴에 "삭제 너가해줘"라고 말했을 때만 통과, 그 외에는 차단한다.
FLAG="${KIMCO_DELETE_FLAG:-/tmp/kimco-delete-allowed}"
if [ -f "$FLAG" ]; then
  exit 0
fi
cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"삭제는 사용자가 \"삭제 너가해줘\"라고 직접 말했을 때만 가능합니다. 상태를 완료/보류로 바꾸거나 사용자에게 삭제를 요청하세요."}}
JSON
