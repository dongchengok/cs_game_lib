package lib.game.cs.sdkservice;

import android.content.Context;
import android.os.Bundle;

import com.ss.android.common.applog.TeaAgent;
import com.ss.android.common.applog.TeaConfigBuilder;
import com.ss.android.common.lib.AppLogNewUtils;
import com.ss.android.common.lib.EventUtils;

public class TouTiao {
    public static void init(Context context){
        TeaAgent.init(TeaConfigBuilder.create(context)
                .setAppName("bcm")
                .setChannel("7001")
                .setAid(153670)
                .createTeaConfig());
        //TeaAgent.setDebug(true);
    }

    public static void setUserUID(String uid){
        TeaAgent.setUserUniqueID(uid);
    }

    public static void onResume(Context context){
        TeaAgent.onResume(context);
    }

    public static void onPause(Context context){
        TeaAgent.onPause(context);
    }

    public static void logRegister(String method, boolean is_success){
        EventUtils.setRegister(method,is_success);
    }

    public static void logPurchase(String type, String name, String id, int num, String channel, String currency, boolean is_sucess, int amount){
        EventUtils.setPurchase(type,name,id,num,channel,currency,is_sucess,amount);
    }

    public static void logEvent(String evt, Bundle params)
    {
        AppLogNewUtils.onEventV3Bundle(evt, params);
    }
}
