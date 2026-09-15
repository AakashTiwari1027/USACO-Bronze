import sys
sys.stdin = open('billboard.in','r')
sys.stdout = open('billboard.out','w')
s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
truck = list(map(int,input().split()))
def inter_area(s1, s2):
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

	return max((min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)),0) * max((min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)),0)

m = (inter_area(truck,s1)+inter_area(truck,s2)-inter_area(s1,s2))
print((abs(s1[0]-s1[2])*abs(s1[1]-s1[3]))+(abs(s2[0]-s2[2])*abs(s2[1]-s2[3]))-m)