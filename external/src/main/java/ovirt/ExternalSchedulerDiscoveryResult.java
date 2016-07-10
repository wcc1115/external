import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class ExternalSchedulerDiscoveryResult {
    private static final Logger log = LoggerFactory.getLogger(ExternalSchedulerDiscoveryResult.class);
    private static final String FILTERS = "filters";
    private static final String SCORES = "scores";
    private static final String BALANCE = "balance";
    private List<Object> filters;
    private List<Object> scores;
    private List<Object> balance;

    ExternalSchedulerDiscoveryResult() {
        filters = new LinkedList<>();
        scores = new LinkedList<>();
        balance = new LinkedList<>();
    }

    public boolean populate(Object xmlRpcRawResult) {
        return true;
    }

    private List<Object> getRelevantList(String type) {
        switch (type) {
        case FILTERS:
            return filters;
        case SCORES:
            return scores;
        case BALANCE:
            return balance;
        default:
            return null;
        }
    }

    List<Object> getFilters() {
        return filters;
    }

    void setFilters(List<Object> filters) {
        this.filters = filters;
    }

    List<Object> getScores() {
        return scores;
    }

    void setScores(List<Object> scores) {
        this.scores = scores;
    }

    List<Object> getBalance() {
        return balance;
    }

    void setBalance(List<Object> balance) {
        this.balance = balance;
    }
}
