import java.io.*;
import java.util.*;
class MyCode {
  public static void main (String[] args) {
    System.out.println("Hello Java");

      char[][] board = new char[][]{
                            { 'X', 'X', 'X', 'X' },
                            { 'X', '0', '0', 'X' },
                            { 'X', 'X', '0', 'X' },
                            { 'X', '0', 'X', 'X' }
                          };
    MyCode x = new MyCode();
    x.captureRegion(board);

    for(int i=0;i<board.length;i++)  {
      for(int j=0;j<board[0].length;j++) {
        System.out.print(board[i][j]);
      }
      System.out.println();
    }
  }
  private static class Node {
        int x;
        int y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return x == node.x &&
                    y == node.y;
        }
        @Override
        public int hashCode() {
            return 31 * x + y;
        }
        @Override
        public String toString() {
            final StringBuilder sb = new StringBuilder("Node{");
            sb.append("x=").append(x);
            sb.append(", y=").append(y);
            sb.append('}');
            return sb.toString();
        }
    }
  private void captureRegion(char[][] board) {
    HashSet<Node> set=new HashSet<Node>();
    for(int i=0;i<board.length;i++)  {
      for(int j=0;j<board[0].length;j++) {
        if(board[i][j]=='0') {
          dfs(board, i, j, set);
        }
      }
    }
  }
  public boolean dfs(char[][] board, int row, int col,HashSet<Node> set) {
    //System.out.println(row +","+ col);

    if(row<0 || row>= board.length || col<0 || col>=board[0].length) {
      return false;
    }

    if(board[row][col] =='X') {
      return true;
    }

    Node x = new Node(row, col);
    if(set.contains(x)) {
      return true;
    }


    set.add(x);
    boolean ans  = dfs(board, row+1, col, set) &&
              dfs(board, row-1, col, set) &&
              dfs(board, row, col+1, set) &&
              dfs(board, row, col-1, set);
    if (ans == true) {
      board[row][col] = 'X';
    }

    return ans;

  }
}
