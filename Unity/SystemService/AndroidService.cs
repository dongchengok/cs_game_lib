namespace CSUnity
{
    /// <summary>
    /// android系统函数
    /// 能不写java插件就不写,都用JNI搞，懒人，用着也省事
    /// </summary>
    public class AndroidService : CommonService
    {
        /// <summary>
        /// 获取android系统版本号
        /// </summary>
        /// <returns>系统版本号，字符串那个</returns>
        public static string GetSDKVersionDisplay ()
        {
            using (var _version = AndroidJavaClass ("android.os.Build.VERSION"))
            {
                return _version.GetStatic<int> ("SDK");
            }
            return "";
        }

        /// <summary>
        /// 获取android系统版本号
        /// </summary>
        /// <returns>系统版本号，整数那个</returns>
        public static int GetSDKVersionInt ()
        {
            using (var _version = AndroidJavaClass ("android.os.Build.VERSION"))
            {
                return _version.GetStatic<int> ("SDK_INT");
            }
            return -1;
        }

        /// <summary>
        /// 检查系统是否授权
        /// </summary>
        /// <param name="name">授权类型</param>
        /// <returns>是否授权</returns>
        public static bool CheckPermission (string name)
        {
            using (AndroidJavaObject _PackageManager = GetActivity ().Call<AndroidJavaObject> ("getPackageManager"))
            {
                string _name = _GetActivity ().Call<string> ("getPackageName");
                int _ret = _PackageManager.Call<int> ("checkPermission", "android.permission.READ_PHONE_STATE", _name);
                return _ret == _PackageManager.GetStatic<int> ("PERMISSION_GRANTED");
            }
        }

        public static string GetSystemProperty(string name)
        {
            using( AndroidJavaClass _SysProps = AndroidJavaClass("android.os.SystemProperties"))
            {
                //_SysProps.CallStatic<string>("get","ril.gsm.imei")

            }
        }

        public static bool SetSystemProperty(string name,string value)
        {
            using( AndroidJavaClass _SysProps = AndroidJavaClass("android.os.SystemProperties"))
            {
                //_SysProps.CallStatic<string>("get","ril.gsm.imei")
                _SysProps.CallStatic<string>("set",name,value);
            }
        }

        /// <summary>
        /// 获取设备IMEI，GSM的唯一识别码
        /// </summary>
        /// <returns>IMEI,如果是多卡手机，返回的IMEI会有多个，并且以，隔开</returns>
        public static string GetIMEI ()
        {
            if(!CheckPermission("TELEPHONY_SERVICE"))
            {
                return "";
            }
            if( GetSDKVersionInt()<21 )
            {
                using (AndroidJavaObject _service = GetSystemService ("TELEPHONY_SERVICE")) {
                    return _service.Call<string> ("getDeviceId");
                }
            }
            else
            {
                using( AndroidJavaClass _props = AndroidJavaClass("android.os.SystemProperties"))
                {
                    string _gsm = _props.CallStatic<string>("ril.gsm.imei","");
                    using (AndroidJavaObject _service = GetSystemService ("TELEPHONY_SERVICE")) {
                        try
                        {
                            
                        }
                        catch(...)
                        {

                        }
                        //return _service.Call<string> ("getDeviceId");
                    }
                }
                }
/*                 using (AndroidJavaObject _service = GetSystemService ("TELEPHONY_SERVICE")) {
                    return _service.Call<string> ("getDeviceId");
                } */
            }
            return "";
        }

        /// <summary>
        /// 获取设备IMEI，GSM的唯一识别码
        /// </summary>
        /// <param name="index">多卡手机的索引</param>
        /// <returns>IMEI</returns>
        public static string GetIMEI (int index)
        {
            string _imei = GetIMEI();
            return "";
        }

        /// <summary>
        /// 获取设备MEID,CDMA手机的唯一识别码
        /// </summary>
        /// <param name="index">多卡手机的索引</param>
        /// <returns>MEID</returns>
        public static string GetMEID ()
        {

        }

        private static AndroidJavaObject _GetActivity ()
        {
            using (var _activity = new AndroidJavaClass ("com.unity3d.player.UnityPlayer"))
            {
                return _activity.GetStatic<AndroidJavaObject> ("currentActivity");
            }
        }

        private static AndroidJavaObject _GetSystemService (string serviceName)
        {
            using (var _context = new AndroidJavaClass ("android.content.Context"))
            {
                AndroidJavaObject _activity = GetActivity ();
                AndroidJavaObject _service = _activity.Call<AndroidJavaObject> ("getSystemService", _context.GetStatic<string> (serviceName));
                return _service;
            }
        }
    }
}