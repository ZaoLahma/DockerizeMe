package com.github.zaolahma.homie.servicediscovery;

import java.io.Serializable;

public class ServiceRepositoryInfo implements Serializable {
    public final String mAddress;
    public final String mPath;
    public final int mPortNo;

    public ServiceRepositoryInfo(String address, int portNo, String path) {
        mAddress = address;
        mPath = path;
        mPortNo = portNo;
    }

    @Override
    public String toString() {

        String retVal =
                "mAddress: " + mAddress +
                        " mPath: " + mPath +
                        " mPortNo: " + mPortNo;

        return retVal;
    }
}
