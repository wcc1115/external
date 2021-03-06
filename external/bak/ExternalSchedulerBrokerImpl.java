package ovirt;

import common.Pair;
import common.Guid;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;
import java.util.Map;

import org.apache.xmlrpc.XmlRpcException;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ExternalSchedulerBrokerImpl implements ExternalSchedulerBroker {

	private static String DISCOVER = "discover";
	private static String FILTER = "runFilters";
	private static String SCORE = "runCostFunctions";
	private static String BALANCE = "runLoadBalancing";

	private static Object[] EMPTY = new Object[] {};

	private final static Logger log = LoggerFactory.getLogger(ExternalSchedulerBrokerImpl.class);

	private XmlRpcClientConfigImpl config = null;

	public ExternalSchedulerBrokerImpl() {
		String extSchedUrl = "http://127.0.0.1:8000";
		config = new XmlRpcClientConfigImpl();
		config.setEnabledForExtensions(true);
		/* wish to be ms */
		config.setConnectionTimeout(3000);
		config.setReplyTimeout(3000);
		try {
			config.setServerURL(new URL(extSchedUrl));
		} catch (MalformedURLException e) {
			log.error("External scheduler got bad url: {}", e.getMessage());
			log.debug("Exception", e);
		}
	}

	@Override
	public ExternalSchedulerDiscoveryResult runDiscover0() {
		try {
			XmlRpcClient client = new XmlRpcClient();
			client.setConfig(config);
			Object result = client.execute(DISCOVER, EMPTY);
			return parseDiscoverResults(result);

		} catch (XmlRpcException e) {
			log.error("Error communicating with the external scheduler while discovering: {}", e.getMessage());
			log.debug("Exception", e);
			return null;
		}
	}

	private ExternalSchedulerDiscoveryResult parseDiscoverResults(Object result) {
		ExternalSchedulerDiscoveryResult retValue = new ExternalSchedulerDiscoveryResult();
		if (!retValue.populate(result)) {
			return null;
		}
		return retValue;
	}

    @Override
    public List<Guid> runFilters(List<String> filterNames,
            List<Guid> hostIDs,
            Guid vmID,
            Map<String, String> propertiesMap) {
       return null;
    }

    private void auditLogFailedToConnect() {
       System.out.println("FailedToConnect");
    }

    private Object[] createFilterArgs(List<String> filterNames,
            List<Guid> hostIDs,
            Guid vmID,
            Map<String, String> propertiesMap) {
        Object[] sentObject = new Object[4];
        // filters name
        sentObject[0] = filterNames;
        // hosts ids
        String[] arr = new String[hostIDs.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = hostIDs.get(i).toString();
        }
        sentObject[1] = arr;
        // vm id
        sentObject[2] = vmID.toString();
        // additional args
        sentObject[3] = propertiesMap;
        return sentObject;
    }

    @Override
    public List<Pair<Guid, Integer>> runScores(List<Pair<String, Integer>> scoreNameAndWeight,
            List<Guid> hostIDs,
            Guid vmID,
            Map<String, String> propertiesMap) {
        return null;
    }

    private Object[] createScoreArgs(List<Pair<String, Integer>> scoreNameAndWeight,
            List<Guid> hostIDs,
            Guid vmID,
            Map<String, String> propertiesMap) {
        Object[] sentObject = new Object[4];

        Object[] pairs = new Object[scoreNameAndWeight.size()];

        for (int i = 0; i < pairs.length; i++) {
            pairs[i] = new Object[] { scoreNameAndWeight.get(i).getFirst(), scoreNameAndWeight.get(i).getSecond() };
        }
        // score name + weight pairs
        sentObject[0] = pairs;
        // hosts ids
        String[] arr = new String[hostIDs.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = hostIDs.get(i).toString();
        }
        sentObject[1] = arr;
        // vm id
        sentObject[2] = vmID.toString();
        // additional args
        sentObject[3] = propertiesMap;

        return sentObject;
    }


    @Override
    public Pair<List<Guid>, Guid> runBalance(String balanceName, List<Guid> hostIDs, Map<String, String> propertiesMap) {
        return null;
    }

    private Object[] createBalanceArgs(String balanceName, List<Guid> hostIDs, Map<String, String> propertiesMap) {
        Object[] sentObject = new Object[3];
        // balance name
        sentObject[0] = balanceName;
        // hosts ids
        String[] arr = new String[hostIDs.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = hostIDs.get(i).toString();
        }
        sentObject[1] = arr;
        // additional args
        sentObject[2] = propertiesMap;

        return sentObject;
    }
}
