# https://leetcode.com/problems/sudoku-solver

class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		n = len(board)
		rows = [set() for _ in range(n)]
		cols = [set() for _ in range(n)]
		boxes = [set() for _ in range(n)]
		emptys = []
		for r in range(n):
			for c in range(n):
				val = board[r][c]
				if val == '.': 
					emptys.append( (r,c) )
					continue
				rows[r].add(val)
				cols[c].add(val)
				idx = (r // 3) * 3 + c // 3
				boxes[idx].add(val)
		def remove(row,col):
			val = board[row][col]
			rows[row].remove(val)
			cols[col].remove(val)
			boxes[(row // 3) * 3 + col // 3].remove(val)
			board[row][col] = '.'
		def check(row,col,val):
			if val in rows[row]: return False
			elif val in cols[col]: return False
			elif val in boxes[(row // 3) * 3 + col // 3]: return False
			return True
		signal = 0
		def backtrack(empty):
			nonlocal signal
			if empty == len(emptys): 
				signal = 1
				return None
			row, col = emptys[empty][0] , emptys[empty][1]
			for i in range(n):
				val = str(i+1)
				if check(row,col,val): 
					board[row][col] = val
					rows[row].add(val)
					cols[col].add(val)
					boxes[(row // 3) * 3 + col // 3].add(val)
					backtrack(empty+1)
					if signal == 0:
						remove(row,col)
			return None
		backtrack(0)