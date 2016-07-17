package ovirt;

import common.Guid;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class ExternalSchedulerBrokerImplTest extends TestCase {
	private static ExternalSchedulerBroker broker = ExternalSchedulerFactory.getInstance();
	public void testRunDiscover() {
		System.out.println("\n------\ntestRunDiscover() entered\n------\n");
		broker.runDiscover();
		System.out.println("\n------\ntestRunDiscover() finished\n------\n");
	}
	public void testRunFilters() {
		System.out.println("\n------\ntestRunFilters() entered\n------\n");
		List<String> filterNames = new ArrayList<String>(Arrays.asList("f1", "f2", "f3"));
		List<Guid> hostIds = new ArrayList<Guid>();
		Guid vmId = new Guid(UUID.randomUUID());
		//System.out.println("A UUID looks like this:" + UUID.randomUUID());
		Map<String, String> properties = new HashMap<String, String>();

		List<Guid> guids = broker.runFilters(filterNames, hostIds, vmId, properties);
		try {
			System.out.println("guids: " + guids.toString());
		} catch (NullPointerException e) {
			System.out.println("guids is null pointer");
		}
		System.out.println("\n------\ntestRunFilters() finished\n------\n");
	}
}
