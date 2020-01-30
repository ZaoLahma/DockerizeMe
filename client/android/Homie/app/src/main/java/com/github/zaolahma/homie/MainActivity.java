package com.github.zaolahma.homie;

import androidx.appcompat.app.AppCompatActivity;

import android.app.PendingIntent;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import com.github.zaolahma.homie.servicediscovery.ServiceDiscoveryRequest;
import com.github.zaolahma.homie.servicediscovery.ServiceRepositoryInfo;

import org.json.JSONException;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private static final int RSS_DOWNLOAD_REQUEST_CODE = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void sendMessage(View view) throws IOException, JSONException {
        System.out.println("Clickety!");

        PendingIntent pendingResult = createPendingResult(
                RSS_DOWNLOAD_REQUEST_CODE, new Intent(), 0);
        Intent intent = new Intent(getApplicationContext(), ServiceDiscoveryRequest.class);
        intent.putExtra(ServiceDiscoveryRequest.MULTICAST_ADDR, "224.3.29.71");
        intent.putExtra(ServiceDiscoveryRequest.PENDING_RESULT_EXTRA, pendingResult);
        startService(intent);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == RSS_DOWNLOAD_REQUEST_CODE) {
            switch (resultCode) {
                case ServiceDiscoveryRequest.ERROR_CODE:
                    break;
                case ServiceDiscoveryRequest.RESULT_CODE:
                    ServiceRepositoryInfo info = (ServiceRepositoryInfo) data.getSerializableExtra(ServiceDiscoveryRequest.SERVICE_REPO_RESULT_EXTRA);
                    System.out.println(info.toString());
                    break;
            }
        }
        super.onActivityResult(requestCode, resultCode, data);
    }
}
