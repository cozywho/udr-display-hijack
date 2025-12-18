#!/bin/sh

#RUN ON ROUTER.

cd /root || exit 1

UI_PID="$(pidof udr-ui)"
[ -z "$UI_PID" ] && exit 1

RUN=1

cleanup() {
  RUN=0
  kill -CONT "$UI_PID" 2>/dev/null
  exit 0
}

trap cleanup INT TERM EXIT

# Pause UI redraws
kill -STOP "$UI_PID"

while [ "$RUN" -eq 1 ]; do
  for f in gits_frames/*.raw; do
    [ "$RUN" -eq 0 ] && break
    dd if="$f" of=/dev/fb0 bs=160 status=none
    sleep 0.08
  done
done

