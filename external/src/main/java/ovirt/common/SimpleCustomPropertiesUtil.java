package common;

public class SimpleCustomPropertiesUtil extends CustomPropertiesUtils {

    private static final SimpleCustomPropertiesUtil instance = new SimpleCustomPropertiesUtil();

    public static SimpleCustomPropertiesUtil getInstance() {
        return instance;
    }
}
