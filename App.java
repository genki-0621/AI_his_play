import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class App {

    public static void main(String[] args) {
        Map<String, Integer> stayTimes = loadStayTimes();

        List<Entry<String, Integer>> sortedPages = sortPages(stayTimes);

        writeCsv(sortedPages, "ranking.csv");

        System.out.println("ランキングCSVを出力しました: ranking.csv");
    }

    public static Map<String, Integer> loadStayTimes() {
        Map<String, Integer> map = new HashMap<>();
        // ダミーデータ
        map.put("DocumentA", 120);
        map.put("DocumentB", 90);
        map.put("DocumentC", 150);
        return map;
    }

    public static List<Entry<String, Integer>> sortPages(Map<String, Integer> pages) {
        List<Entry<String, Integer>> list = new ArrayList<>(pages.entrySet());
        list.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));
        return list;
    }

    public static void writeCsv(List<Entry<String, Integer>> sortedPages, String filepath) {
        try (PrintWriter pw = new PrintWriter(new FileWriter(filepath))) {
            pw.println("順位,ページ,滞在時間(秒)");
            int rank = 1;
            for (Entry<String, Integer> entry : sortedPages) {
                pw.printf("%d,%s,%d%n", rank++, entry.getKey(), entry.getValue());
            }
        } catch (IOException e) {
            System.err.println("CSV出力エラー: " + e.getMessage());
        }
    }
}

