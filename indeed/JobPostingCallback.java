import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Stack;
import java.net.MalformedURLException;
import java.net.URL;

import javax.swing.text.MutableAttributeSet;
import javax.swing.text.html.HTML.Attribute;
import javax.swing.text.html.HTML.Tag;
import javax.swing.text.html.HTMLEditorKit;


public class JobPostingCallback extends HTMLEditorKit.ParserCallback {

	Stack<String> tagstack;
	ArrayList<LinkedHashMap<String, String>> results;
	LinkedHashMap<String, String> jobDetails;
	int seenTDs = 0;
	boolean start = false;
	String baseUrl = "";
	
	public JobPostingCallback() {
		tagstack = new Stack<String>();
		jobDetails = new LinkedHashMap<String, String>();
	}
	
	public JobPostingCallback(ArrayList<LinkedHashMap<String, String>> results, String url) {
		tagstack = new Stack<String>();
		jobDetails = new LinkedHashMap<String, String>();
		this.results = results;
		baseUrl = buildBaseURL(url);
	}
	
	private String buildBaseURL(String url) {
		String baseUrl = "";
		try {
			URL givenUrl = new URL(url);
			baseUrl = givenUrl.getProtocol() + "://" + givenUrl.getHost();
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}
		
		return baseUrl;
	}
	
	private String charArrayToString(char[] data) {
		StringBuilder sb = new StringBuilder();
		for(char d : data) {
			sb.append(d);
		}
		
		return sb.toString();
	}
	
	@Override
	public void handleText(char[] data, int pos) {
		super.handleText(data, pos);
		if(start) {
			if(tagstack.size() > 0) {
				if("a".equals(tagstack.peek())) {
					jobDetails.put("title", charArrayToString(data));
				}
				
				if("td".equals(tagstack.peek())) {
					seenTDs = seenTDs + 1;
					if(seenTDs == 3) {
						jobDetails.put("location", charArrayToString(data));
						seenTDs = 0;
					}
				}
			}
		}
	}

	@Override
	public void handleStartTag(Tag t, MutableAttributeSet a, int pos) {
		super.handleStartTag(t, a, pos);
		if("table".equals(t.toString())) {
			tagstack.push(t.toString());
			String id = (String) a.getAttribute(Attribute.ID);
			if("job-opportunity".equals(id)) {
				start = true;
			}
		}
		
		if(start) {
			if("tr".equals(t.toString())) {
				tagstack.push(t.toString());
			}
			
			if("td".equals(t.toString())) {
				tagstack.push(t.toString());
			}
			
			if(tagstack.size() > 0 && "td".equals(tagstack.peek()) && "a".equals(t.toString())) {
				tagstack.push(t.toString());
				jobDetails = new LinkedHashMap<String, String>();
				jobDetails.put("url", baseUrl + (String) a.getAttribute(Attribute.HREF));
			}
		}
		
	}

	@Override
	public void handleEndTag(Tag t, int pos) {
		super.handleEndTag(t, pos);
		if(start) {
			if(tagstack.size() > 0) {
				if("tr".equals(t.toString())) {
					if(!jobDetails.isEmpty())
						results.add(jobDetails);
					tagstack.pop();
				}
				
				if("td".equals(t.toString())) {
					tagstack.pop();
				}
				
				if("a".equals(t.toString())) {
					tagstack.pop();
				}
			}
		}
	}

}
