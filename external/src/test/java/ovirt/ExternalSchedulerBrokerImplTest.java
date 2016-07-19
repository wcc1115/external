package ovirt;

import common.Guid;
import common.Pair;

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

	public void testRunScores() {
		System.out.println("\n------\ntestRunScores() entered\n------\n");

		List<Pair<String, Integer>> scoreNameAndWeight = new ArrayList<Pair<String, Integer>>(
			Arrays.asList(new Pair<String, Integer>("score1", 101), new Pair<String, Integer>("score2", 102), new Pair<String, Integer>("score3", 103)));
		List<Guid> hostIds = new ArrayList<Guid>();
		Guid vmId = new Guid(UUID.randomUUID());
		Map<String, String> properties = new HashMap<String, String>();

		List<Pair<Guid, Integer>> hostIdAndScore = broker.runScores(scoreNameAndWeight, hostIds, vmId, properties);

		try {
			System.out.println("hostIdAndScore:\n" + hostIdAndScore.toString());
		} catch (NullPointerException e) {
			System.out.println("hostIdAndScore is null pointer");
		}

		System.out.println("\n------\ntestRunScores() finished\n------\n");
	}

	public void testRunBalance() {
		System.out.println("\n------\ntestRunLoadBalancing() entered\n------\n");
		
		String name = "testLoadBalancingFunction";
		List<Guid> hids = new ArrayList<Guid>(3);
		for (int i = 0; i < 3; ++i) {
			hids.add(new Guid(UUID.randomUUID()));
		}
		Map<String, String> properties = new HashMap<String, String>();

		Pair<List<Guid>, Guid> hostsAndVm = broker.runBalance(name, hids, properties);

		try {
			System.out.println("load balancing targets: " + hostsAndVm.getFirst().toString());
			System.out.println("load balancing vm: " + hostsAndVm.getSecond().toString());
		} catch (NullPointerException e) {
			System.out.println("hostsAndVm is null pointer");
		}

		System.out.println("\n------\ntestRunLoadBalancing() finished\n------\n");
	}
}
