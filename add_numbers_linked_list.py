from linked_list import Node

def sum(n1, n2):
	carry = 0
	sum = Node(None)
	while n1 is not None or n2 is not None:
		cur_sum = carry
		if n1 is not None:
			cur_sum += n1.value
			n1 = n1.next
		if n2 is not None:
			cur_sum += n2.value
			n2 = n2.next
		carry = cur_sum / 10
		sum.add_to_tail(cur_sum % 10)
	if carry > 0:
		sum.add_to_tail(carry)
	return sum.next

#################### DRIVERS ####################

if __name__ == "__main__":
	num1 = Node(9).add_to_tail(9, 9)
	num2 = Node(9).add_to_tail(9, 9)
	num1 = Node(1).add_to_tail(1)
	num2 = Node(1)
	sum(num1, num2).print_list()
