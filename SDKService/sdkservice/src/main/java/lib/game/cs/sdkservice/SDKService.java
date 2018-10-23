package lib.game.cs.sdkservice;

import android.content.Context;
import android.os.Bundle;

public class SDKService {
    public static void init(Context context){
        TouTiao.init(context);
    }

    public static void setUserUID(String uid){
        TouTiao.setUserUID(uid);
    }

    public static void onResume(Context context){
        TouTiao.onResume(context);
    }

    public static void onPause(Context context){
        TouTiao.onPause(context);
    }

    public static Bundle newLogParams()
    {
        return new Bundle();
    }

    public static void logEvent(String evt, Bundle params)
    {
        TouTiao.logEvent(evt,params);
    }

    public static void logRegister(String method, boolean is_success){
        TouTiao.logRegister(method,is_success);
    }

    public static void logPurchase(String type, String name, String id, int num, String channel, String currency, boolean is_sucess, int amount){
        TouTiao.logPurchase(type,name,id,num,channel,currency,is_sucess,amount);
    }
}
