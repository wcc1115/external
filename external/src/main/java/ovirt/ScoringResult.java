package ovirt;

import java.util.ArrayList;
import java.util.List;

import common.Guid;
import common.Pair;

public class ScoringResult extends SchedulerResult {
    private List<Pair<Guid, Integer>> hostsWithScores;

    public void addHost(Guid host, Integer score) {
        if (hostsWithScores == null) {
            hostsWithScores = new ArrayList<>();
        }

        hostsWithScores.add(new Pair<>(host, score));
    }

    public List<Pair<Guid, Integer>> getHosts() {
        return hostsWithScores;
    }
}
