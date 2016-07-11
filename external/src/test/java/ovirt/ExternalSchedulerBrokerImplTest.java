package ovirt;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class ExternalSchedulerBrokerImplTest extends TestCase {
	private static ExternalSchedulerBroker broker = ExternalSchedulerFactory.getInstance();
	public void testRunDiscover() {
		broker.runDiscover();
	}
}
