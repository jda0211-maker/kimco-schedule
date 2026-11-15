#!/usr/bin/env bash
# 삭제 계열 도구 호출을 완전 차단한다.
cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"삭제는 차단되어 있습니다. 상태를 완료/보류로 바꾸고, 실제 삭제는 사용자가 직접 하세요."}}
JSON
