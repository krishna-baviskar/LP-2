import java.util.*;

class Graph { 
    int V;
    ArrayList<Integer>[] adj;

    Graph(int V) {
        this.V = V;
        adj = new ArrayList[V];
        for (int i = 0; i < V; i++)
            adj[i] = new ArrayList<>();
    }

    void addEdge(int u, int v) {
        adj[u].add(v);
        adj[v].add(u);   
    }

  
    void dfs(int v, boolean[] visited) {
        visited[v] = true;
        System.out.print(v + " ");
        for (int n : adj[v])
            if (!visited[n])
                dfs(n, visited);
    }

  
    void bfs(int s) {
        boolean[] visited = new boolean[V];
        Queue<Integer> q = new LinkedList<>();

        visited[s] = true;
        q.add(s);

        while (!q.isEmpty()) {
            int v = q.poll();
            System.out.print(v + " ");
            for (int n : adj[v])
                if (!visited[n]) {
                    visited[n] = true;
                    q.add(n);
                }
        }
    }

    public static void main(String[] args) {
        Graph g = new Graph(5);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(1, 4);

        boolean[] visited = new boolean[5];
        System.out.print("DFS: ");
        g.dfs(0, visited);

        System.out.print("\nBFS: ");
        g.bfs(0);
    }
}

