import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.LinkedHashMap;

import javax.swing.text.html.HTMLEditorKit;
import javax.swing.text.html.parser.ParserDelegator;

public class IndeedJobTest {
	
	public static ArrayList<?> scrape(String url) throws IOException {
		ArrayList<LinkedHashMap<String, String>> jobs = new ArrayList<LinkedHashMap<String, String>>();
		try {
			URL urlToScrape = new URL(url);
			URLConnection connection = urlToScrape.openConnection();
			HTMLEditorKit.ParserCallback callback = new JobPostingCallback(jobs, url);
			BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()));
			ParserDelegator delegator = new ParserDelegator();
			delegator.parse(br, callback, true);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		return jobs;
	}
	
	public static void main(String[] args) {
		LinkedHashMap<String, String> expected = new LinkedHashMap<String, String>();
		expected.put("url", "http://web.archive.org/web/20150205160442/http://www.besmith.com/candidates/job-opportunities/director-invasive-cardiology");
		expected.put("title", "Director, Invasive Cardiology");
		expected.put("location", "Bryan, Texas");
		String testUrl = "http://web.archive.org/web/20150205160442/http://www.besmith.com/candidates/search?page=1";
		try {
			ArrayList<LinkedHashMap<String, String>> results = (ArrayList<LinkedHashMap<String, String>>) scrape(testUrl);
			LinkedHashMap<String, String> first = results.get(0);
			if(first.values().containsAll(expected.values())) {
				System.out.println("Success!");
			} else {
				System.out.println("Fail!");
			}
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
	}
} 