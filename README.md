# AI-pacman-search


Cách làm các question

Q1:dfs
  - Sử dụng stack() lưu các successors 
  - Mỗi 1 phần tử stack sẽ lưu state và các bước để đến state đó
  - Sử dụng list để lưu các state đã đi qua
  - các successors có state nằm trong list thì sẽ không được cho vào stack
  
Q2:bfs
  - Sử dụng queue() lưu các successors 
  - Mỗi 1 phần tử queue sẽ lưu state và các bước để đến state đó
  - Sử dụng list để lưu các state đã đi qua
  - các successors có state nằm trong list thì sẽ không được cho vào queue
  
Q3:ucs
  - Sử dụng PriorityQueue() lưu các successors, ưu tiên chi phí thấp
  - Mỗi 1 phần tử PriorityQueue() sẽ lưu state,các bước để đến state đó và chi phí thực hiện để đến bước đó
  - Sử dụng list để lưu các state đã đi qua và chi phí
  - các successors có state nằm trong list thì néu chi phí mới lớn hơn chi phí cũ thì bị loại bỏ, không thì sẽ thay thế cái cũ , đồng thời đưa vào queue
  
Q4:astar
  - Sử dụng PriorityQueue() lưu các successors, ưu tiên chi phí + heuristic thấp
  - Mỗi 1 phần tử PriorityQueue() sẽ lưu state,các bước để đến state đó, chi phí thực hiện để đến bước đó, tổng chi phí + heuristic
  - Sử dụng list để lưu các state đã đi qua và chi phí
  - các successors có state nằm trong list thì néu chi phí mới lớn hơn chi phí cũ thì bị loại bỏ, không thì sẽ thay thế cái cũ , đồng thời đưa vào queue
  
Q5:cornersProblem
  - thêm biến list checkList kiểm tra đã đến 4 góc chưa ([0,0,0,0] -> [1,1,1,1]) vào thông tin trạng thái state
  - hàm isGoal khi biến kiểm tra là [1,1,1,1]
  
Q6:cornersHeuristic
  - khởi tạo heuristic = 0
  - chỉ số Heuristic được tính bằng:
    + tạo bản sao của checkList và pacmanPosition
    + cộng với khoảng cách mahattan từ pacmanPosition đến góc gần nhất chưa đi đến
    + di chuyển pacmanPosition(copy) đến vị trí vừa đến
    + lặp lại các bước đến khi checkList(copy) thỏa mãn == [1,1,1,1]
    
Q7:eat all dot
  - xây dựng foodHeuristic:
    + Sử dụng hàm MazeDistance ( ở cuối cùng file), là hàm trả về khoảng cách ngắn nhât giữa 2 vị trí, và phụ thuộc vào map (tìm kiếm theo thuật toán bfs)
    + foodHeuristic là khoảng cách MazeDistance dài nhất giữa state.position đến các dot ( khoảng cách từ pacman đến dot xa nhất)
    
Q8:closestDot
    - xây dựng hoàn toàn giống như bfs
    - isgoal trả về true khi pacman position là 1 trong food.asList()
    
  
