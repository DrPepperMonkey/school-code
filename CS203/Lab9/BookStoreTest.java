

import static org.junit.Assert.*; 
import org.junit.Before;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class BookStoreTest {

	private BookStore store;
	private Book b1 = new Book(1, "Harper Lee", "To Kill a Mockingbird");
	private Book b2 = new Book(2, "Harper Lee", "To Kill a Mockingbird");
	private Book b3 = new Book(3, "Frances Hodgson", "The Secret Garden");
	private Book b4 = new Book(5, "J.K. Rowling",
			"Harry Potter and the Sorcerer's Stone");
	private Book b5 = new Book(4, "Douglas Adams",
			"The Hitchhiker's Guide to the Galaxy");
	private Book b6 = new Book(6, "Harper Lee", "To Kill a Mockingbird");


	/**
	 * setup the store
	 * 
	 */
	@Before
	public void setUpBookStore() {
		store = new BookStore();
		store.addBook(b1);
		store.addBook(b2);
		store.addBook(b3);
		store.addBook(b4);
		store.addBook(b5);

	}

	/**
	 * tests the addition of book
	 * 
	 */

	@Test
	public void testAddBook() {
		store.addBook(b6);
		assertTrue(store.getBooks().contains(b6));

	}

	/**
	 * tests the deletion of book
	 * 
	 */

	@Test
	public void testDeleteBook() {
		store.deleteBook(b1);
		assertFalse(store.getBooks().contains(b1));
	}

	/**
	 * tests sorting of books by author name
	 * 
	 */

	@Test
	public void testGetBooksSortedByAuthor() {
		BookStore sorted = new BookStore();
		sorted.addBook(b5);
		sorted.addBook(b3);
		sorted.addBook(b1);
		sorted.addBook(b2);
		sorted.addBook(b4);
		assertEquals(sorted.getBooks(), store.getBooksSortedByAuthor());
		
	}

	/**
	 * tests sorting of books by title
	 * 
	 */

	@Test
	public void testGetBooksSortedByTitle() {
		BookStore sorted = new BookStore();
		sorted.addBook(b4);
		sorted.addBook(b5);
		sorted.addBook(b3);
		sorted.addBook(b1);
		sorted.addBook(b2);
		assertEquals(sorted.getBooks(), store.getBooksSortedByTitle());
	}

	/**
	 * tests the number of copies of book in store
	 * 
	 */

	@Test
	public void testCountBookWithTitle() {
		store.addBook(b6);
		assertEquals(3, store.countBookWithTitle("To Kill a Mockingbird"));
	}

	/**
	 * tests returning of book list
	 */
	@Test
	public void testGetBook() {
		List<Book> newStore = new ArrayList<Book>();
		newStore.add(b1);
		newStore.add(b2);
		newStore.add(b3);
		newStore.add(b4);
		newStore.add(b5);
		assertEquals(newStore, store.getBooks());
	}
}
