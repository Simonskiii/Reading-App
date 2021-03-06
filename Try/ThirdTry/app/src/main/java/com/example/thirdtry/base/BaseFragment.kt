package com.example.thirdtry.base

import android.content.Context
import android.os.Bundle
import android.os.Handler
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.annotation.LayoutRes
import androidx.annotation.NonNull
import androidx.fragment.app.Fragment
import com.classic.common.MultipleStatusView
import kotlinx.android.synthetic.main.article_fragment.*
import pub.devrel.easypermissions.AppSettingsDialog
import pub.devrel.easypermissions.EasyPermissions


abstract class BaseFragment: Fragment(),EasyPermissions.PermissionCallbacks{
    private var isFirstLoad = true // 是否第一次加载
    protected lateinit var token :String
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val s = activity?.getSharedPreferences("loginToken", 0)
        token = s?.getString("token", "").toString()
        return inflater.inflate(getLayoutId(), container, false)
    }

    override fun onResume() {
        super.onResume()
        if(isFirstLoad){
            initView()
            initViewModel()
            isFirstLoad = false
        }

    }
    /**
     * 加载布局
     */
    @LayoutRes
    abstract fun getLayoutId():Int

    /**
     * 初始化 View
     */
    abstract fun initView()

    /**
     * 初始化 ViewModel
     */
    abstract fun initViewModel()
//    override fun onDestroy() {
//        super.onDestroy()
//        activity?.let { MyApplication.getRefWatcher(it).watch(activity) }
//    }


    /**
     * 重写要申请权限的Activity或者Fragment的onRequestPermissionsResult()方法，
     * 在里面调用EasyPermissions.onRequestPermissionsResult()，实现回调。
     *
     * @param requestCode  权限请求的识别码
     * @param permissions  申请的权限
     * @param grantResults 授权结果
     */
    override fun onRequestPermissionsResult(requestCode: Int, @NonNull permissions: Array<String>, @NonNull grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        EasyPermissions.onRequestPermissionsResult(requestCode, permissions, grantResults, this)
    }

    /**
     * 当权限被成功申请的时候执行回调
     *
     * @param requestCode 权限请求的识别码
     * @param perms       申请的权限的名字
     */
    override fun onPermissionsGranted(requestCode: Int, perms: List<String>) {
        Log.i("EasyPermissions", "获取成功的权限$perms")
    }

    /**
     * 当权限申请失败的时候执行的回调
     *
     * @param requestCode 权限请求的识别码
     * @param perms       申请的权限的名字
     */
    override fun onPermissionsDenied(requestCode: Int, perms: List<String>) {
        //处理权限名字字符串
        val sb = StringBuffer()
        for (str in perms) {
            sb.append(str)
            sb.append("\n")
        }
        sb.replace(sb.length - 2, sb.length, "")
        //用户点击拒绝并不在询问时候调用
        if (EasyPermissions.somePermissionPermanentlyDenied(this, perms)) {
            Toast.makeText(activity, "已拒绝权限" + sb + "并不再询问", Toast.LENGTH_SHORT).show()
            AppSettingsDialog.Builder(this)
                    .setRationale("此功能需要" + sb + "权限，否则无法正常使用，是否打开设置")
                    .setPositiveButton("好")
                    .setNegativeButton("不行")
                    .build()
                    .show()
        }
    }

}
