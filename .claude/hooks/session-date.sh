#!/usr/bin/env bash
# 세션 시작 시 오늘 날짜(KST)를 컨텍스트로 주입한다.
d=$(TZ=Asia/Seoul date '+%Y-%m-%d')
w=$(TZ=Asia/Seoul date '+%A')
echo "오늘은 ${d} (${w}), 기준 시간대는 KST(Asia/Seoul)입니다."
