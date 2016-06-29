#!/bin/csh
echo "pa2 cs315001s15: MST Kruskals Algorithm"
echo "------------------"
echo "output expected: 3 9"
echo "output computed"
./pa2m2cs315s15 in1.in
echo "------------------"
echo "output expected: 3 12"
echo "output computed"
./pa2m2cs315s15 in2.in
echo "------------------"
echo "output expected: 4 16"
echo "output computed"
./pa2m2cs315s15 in3.in
echo "------------------"
echo "output expected: 8 14"
echo "output computed"
./pa2m2cs315s15 in9.in
echo "------------------"
echo "output expected: 8 14"
echo "output computed"
./pa2m2cs315s15 in9c.in
echo "------------------"
echo "output expected: 8 19"
echo "output computed"
./pa2m2cs315s15 in9d.in
echo "------------------"
echo "output expected: 99 1533"
echo "output computed"
./pa2m2cs315s15 in100.in
echo "------------------"
echo "output expected: 100 100"
echo "output computed"
./pa2m2cs315s15 in100c.in
echo "------------------"
echo "output expected: 99 200"
echo "output computed"
./pa2m2cs315s15 in100e.in
echo "output expected: IMPOSSIBLE"
echo "output computed"
./pa2m2cs315s15 mstEC.txt
echo "----END-----------"
