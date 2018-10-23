package lib.game.cs.sdkservice;

import android.os.Bundle;
import com.unity3d.player.UnityPlayerActivity;

public class UnityPlayerWithSDK extends UnityPlayerActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        SDKService.init(this);
    }

    @Override
    protected void onResume(){
        super.onResume();
        SDKService.onResume(this);
    }

    @Override
    protected void onPause(){
        super.onPause();
        SDKService.onPause(this);
    }
}
