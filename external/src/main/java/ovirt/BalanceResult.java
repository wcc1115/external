package ovirt;

import java.util.ArrayList;
import java.util.List;

import common.Pair;
import common.Guid;


public class BalanceResult extends SchedulerResult {
    private List<Guid> underUtilizedHosts;
    private Guid vmToMigrate = null;
    private Pair<List<Guid>, Guid> balancingData;

    public void addHost(Guid host) {
        if (underUtilizedHosts == null) {
            underUtilizedHosts = new ArrayList<>();
        }

        underUtilizedHosts.add(host);
    }

    public void setVmToMigrate(Guid vm) {
        this.vmToMigrate = vm;
    }


    public Pair<List<Guid>, Guid> getResult() {
        if (balancingData == null) {
            balancingData = new Pair<>(underUtilizedHosts, vmToMigrate);
        }

        return balancingData;
    }
}
