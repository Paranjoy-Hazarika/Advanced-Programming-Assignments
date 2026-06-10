import java.util.ArrayList;
import java.util.Scanner;

public class Book {
  public static void main(String[] args) {
    ArrayList<String> books = new ArrayList<>();

    books.add("The Silent Patient");
    books.add("Diary of a Wimpy Kid");
    books.add("Lord of the Rings");
    books.add("Ikigai");
    books.add("Diary of Anne Frank");

    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter the word to search for the book titles: ");
    String searchWord = scanner.nextLine().toLowerCase();

    boolean found = false;
    System.out.println("\nBooks containing the\"" + searchWord + "\": ");

    for (String book: books) {
      if (book.toLowerCase().contains(searchWord)) {
        System.out.print("-" + book + "\n");
        found = true;
      }
    }

    if (!found) {
      System.out.println("No boooks found with this searchWord" + searchWord);
    }

    scanner.close();
  }
}