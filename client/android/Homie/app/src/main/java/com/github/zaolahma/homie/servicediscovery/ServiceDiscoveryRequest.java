package com.github.zaolahma.homie.servicediscovery;

import android.app.IntentService;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;

import androidx.annotation.Nullable;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.SocketTimeoutException;

public class ServiceDiscoveryRequest extends IntentService {

    public static final String PENDING_RESULT_EXTRA = "pending-result";
    public static final String MULTICAST_ADDR = "multicast-addr";
    public static final String SERVICE_REPO_RESULT_EXTRA = "service-repo-result";

    public static final int RESULT_CODE = 0;
    public static final int ERROR_CODE = 2;

    private static final String TAG = ServiceDiscoveryRequest.class.getSimpleName();

    public ServiceDiscoveryRequest() {
        super(TAG);
    }

    @Override
    protected void onHandleIntent(@Nullable Intent intent) {
        PendingIntent reply = intent.getParcelableExtra(PENDING_RESULT_EXTRA);

        DatagramSocket socket = null;
        try {
            try {
                final String multicastAddress = intent.getStringExtra(MULTICAST_ADDR);

                socket = new DatagramSocket();

                socket.setSoTimeout(2000);

                InetAddress inetAddress = InetAddress.getByName(multicastAddress);

                JSONObject request = new JSONObject();
                request.put(ServiceDiscoveryCommonConstants.REQUEST, ServiceDiscoveryCommonConstants.REQUEST_SERVICE_REPOSITORY_ADDRESS);

                String message = request.toString();

                System.out.println("Sending: " + message);

                byte[] messageBytes = message.getBytes();

                socket.send(new DatagramPacket(messageBytes, messageBytes.length, inetAddress, 4070));

                byte[] responseBuf = new byte[1024];
                DatagramPacket response = new DatagramPacket(responseBuf, responseBuf.length);

                socket.receive(response);

                JSONObject responseJson = new JSONObject(new String(response.getData()));

                System.out.println("ServiceDiscoveryRequest received response " + responseJson);

                JSONObject serviceResponse = responseJson.getJSONObject(ServiceDiscoveryCommonConstants.RESPONSE);


                final String serviceAddress = serviceResponse.getString(ServiceDiscoveryCommonConstants.ADDRESS);
                final int servicePortNo = serviceResponse.getInt(ServiceDiscoveryCommonConstants.PORT_NO);
                final String servicePath = serviceResponse.getString(ServiceDiscoveryCommonConstants.PATH);

                ServiceRepositoryInfo retVal = new ServiceRepositoryInfo(serviceAddress, servicePortNo, servicePath);

                socket.close();

                Intent result = new Intent();
                result.putExtra(SERVICE_REPO_RESULT_EXTRA, retVal);

                reply.send(this, RESULT_CODE, result);

            } catch (JSONException | IOException e) {
                e.printStackTrace();
                reply.send(ERROR_CODE);
            }
        }catch (PendingIntent.CanceledException e) {
            e.printStackTrace();
        }
    }
}
