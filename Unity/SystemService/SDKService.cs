using System.Collections.Generic;

namespace CSUnity
{
    class SDKService
    {
        public class Params
        {
            List<KeyValuePair<string,string>> mParams = new List<KeyValuePair<string,string>>();

            public Put(string key, string value)
            {
                mParams.Add(new KeyValuePair<string,string>(key,value));
            }
        }
        public void Init()
        {

        }

        public void SignIn(Action<string> callback=null)
        {
            
        }

        public void SignOut(Action<string> callback=null)
        {

        }

        public void LogEvent(string name, Params params=null)
        {
            using(AndroidJavaClass sdk = AndroidJavaClass("lib.game.cs.sdkservice.SDKService"))
            {
                using(AndroidJavaObject params = sdk.CallStatic<AndroidJavaObject>("newLogParams")
                {
                    foreach (var item in params.mParams)
                    {
                        params.Call("putString",item.key,item.value);
                    }
                    sdk.CallStatic("logEvent",name,params);
                }
            }
        }

        public void LogRegister(string method, bool is_success)
        {
            using(AndroidJavaClass sdk = AndroidJavaClass("lib.game.cs.sdkservice.SDKService"))
            {
                sdk.CallStatic("logRegister",method,is_success);
            }
        }

        public void LogPurchase(string type, string name, string id, int num, string channel, string currency, bool is_sucess, int amount)
        {
            using(AndroidJavaClass sdk = AndroidJavaClass("lib.game.cs.sdkservice.SDKService"))
            {
                sdk.CallStatic("logPurchase",type,name,id,num,channel,currency,is_success,amount);
            }
        }
    }
}