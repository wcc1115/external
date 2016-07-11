package ovirt;

public class ExternalSchedulerFactory {
    private final static ExternalSchedulerBrokerImpl instance = new ExternalSchedulerBrokerImpl();

    public static ExternalSchedulerBroker getInstance() {
        return instance;
    }
}
