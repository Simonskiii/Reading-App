package com.example.thirdtry.ui.activity.register

import android.annotation.SuppressLint
import android.app.Activity
import android.app.DatePickerDialog
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.view.inputmethod.EditorInfo
import android.widget.CheckBox
import android.widget.Toast
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.example.thirdtry.R
import com.example.thirdtry.ui.activity.login.LoginActivity
import com.example.thirdtry.utils.afterTextChanged
import kotlinx.android.synthetic.main.activity_edit_information.*
import kotlinx.android.synthetic.main.activity_register.*
import kotlinx.android.synthetic.main.activity_register.checkbox_four
import kotlinx.android.synthetic.main.activity_register.checkbox_one
import kotlinx.android.synthetic.main.activity_register.checkbox_three
import kotlinx.android.synthetic.main.activity_register.checkbox_two
import kotlinx.android.synthetic.main.activity_register.loading
import kotlinx.android.synthetic.main.activity_register.password
import kotlinx.android.synthetic.main.activity_register.radio_group
import kotlinx.android.synthetic.main.activity_register.register
import kotlinx.android.synthetic.main.activity_register.username
import java.util.*

class RegisterActivity : AppCompatActivity() {
    companion object {
        var instance: RegisterActivity? = null
    }
    private val calendar = Calendar.getInstance()
    private var checkBoxList = mutableListOf<CheckBox>()
    private lateinit var registerViewModel: RegisterViewModel
    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        instance = this
        setContentView(R.layout.activity_register)
        registerViewModel = ViewModelProviders.of(this, RegisterViewModelFactory())
            .get(RegisterViewModel::class.java)
        var year = calendar.get(Calendar.YEAR)
        var month = calendar.get(Calendar.MONTH) + 1
        var day = calendar.get(Calendar.DATE)
        var gender = "male"
        var birthday = "1999-11-22"
        checkBoxList.add(checkbox_one)
        checkBoxList.add(checkbox_two)
        checkBoxList.add(checkbox_three)
        checkBoxList.add(checkbox_four)
        radio_group.setOnCheckedChangeListener { group, checkedId ->
            when (checkedId) {
                R.id.radio_button_one -> gender = "male"
                R.id.radio_button_two -> gender = "female"
            }
        }
        birthday_tv.setOnClickListener {
            DatePickerDialog(
                this,
                DatePickerDialog.OnDateSetListener { datePicker, i, i1, i2 ->
                    year = i
                    month = i1 + 1
                    day = i2
                    birthday_tv.text = "$year-$month-$day"
                }, year, month, day
            ).show()
        }
        //app中editText的账号密码规范检查
        registerViewModel.registerFormState.observe(this@RegisterActivity, Observer {
            val registerState = it ?: return@Observer
            // disable register button unless both username / password is valid
            register.isEnabled = registerState.isDataValid

            if (registerState.usernameError != null) {
                username.error = getString(registerState.usernameError)
            }
            if (registerState.passwordError != null) {
                password.error = getString(registerState.passwordError)
            }
            if (registerState.emailError != null) {
                email.error = getString(registerState.emailError)
            }
            if (registerState.codeError != null) {
                verify_code.error = getString(registerState.codeError)
            }
        })
        registerViewModel.emailFormState.observe(this@RegisterActivity, Observer{
            val emailState = it ?: return@Observer
            verify.isEnabled = emailState.isEmailValid
        })
        username.afterTextChanged {
            registerViewModel.registerDataChanged(
                username.text.toString(),
                password.text.toString(),
                email.text.toString(),
                verify_code.text.toString()
            )
        }
        password.afterTextChanged {
            registerViewModel.registerDataChanged(
                username.text.toString(),
                password.text.toString(),
                email.text.toString(),
                verify_code.text.toString()
            )
        }
        email.afterTextChanged {
            registerViewModel.registerDataChanged(
                username.text.toString(),
                password.text.toString(),
                email.text.toString(),
                verify_code.text.toString()
            )
            registerViewModel.emailDataChanged(
                email.text.toString()
            )
            verify.setOnClickListener {
                loading.visibility = View.VISIBLE
                //发出post请求并对response进行观察
                registerViewModel.verifyRequest(email.text.toString())
                    .observe(this@RegisterActivity, Observer{
                        if (it == null){
                            Toast.makeText(this@RegisterActivity, "网络开小差了，请稍后", Toast.LENGTH_LONG).show()
                            loading.visibility = View.GONE
                            return@Observer
                        }
                        else{
                            registerViewModel.getVerifyResult(it)
                        }
                    })
            }
        }
        verify_code.apply {
            //password输入时，实时将值传入，以检测是否规范
            afterTextChanged {
                registerViewModel.registerDataChanged(
                    username.text.toString(),
                    password.text.toString(),
                    email.text.toString(),
                    verify_code.text.toString()
                )
            }
            setOnEditorActionListener { _, actionId, _ ->
                val stringBuffer = StringBuffer()
                for (c in checkBoxList) {
                    if (c.isChecked) {
                        when (c.text){
                            "湿气重"->stringBuffer.append("sqz ")
                            "睡眠质量差"->stringBuffer.append("poor_sleep ")
                            "脱发"->stringBuffer.append("little_hair ")
                            "免疫力低下"->stringBuffer.append("low_dkl ")
                        }
                    }
                }
                when (actionId) {
                    EditorInfo.IME_ACTION_DONE ->
                        //发出post请求并对response进行观察

                        registerViewModel.registerRequest(username.text.toString(),password.text.toString(),
                            email.text.toString(),verify_code.text.toString(),birthday = birthday_tv.text.toString(),gender = gender, typ = stringBuffer.toString().trim())
                            .observe(this@RegisterActivity, Observer{
                                if (it == null){
                                    Toast.makeText(this@RegisterActivity, "网络开小差了，请稍后", Toast.LENGTH_SHORT).show()
                                    loading.visibility = View.GONE
                                    return@Observer
                                }
                                else{
                                    registerViewModel.getRegisterResult(it)
                                }

                            })

                }
                false
            }
            //对登录按钮进行绑定

            register.setOnClickListener {
                loading.visibility = View.VISIBLE
                //发出post请求并对response进行观察
                val stringBuffer = StringBuffer()
                for (c in checkBoxList) {
                    if (c.isChecked) {
                        when (c.text){
                            "湿气重"->stringBuffer.append("sqz ")
                            "睡眠质量差"->stringBuffer.append("poor_sleep ")
                            "脱发"->stringBuffer.append("little_hair ")
                            "免疫力低下"->stringBuffer.append("low_dkl ")
                        }
                    }
                }
                registerViewModel.registerRequest(username.text.toString(),password.text.toString(),
                    email.text.toString(),verify_code.text.toString(),birthday = birthday_tv.text.toString(),gender = gender, typ = stringBuffer.toString().trim())
                    .observe(this@RegisterActivity, Observer{
                        if (it == null){
                            Toast.makeText(this@RegisterActivity, "网络开小差了，请稍后", Toast.LENGTH_SHORT).show()
                            loading.visibility = View.GONE
                            return@Observer
                        }
                        else{
                            registerViewModel.getRegisterResult(it)
                        }
                    })
            }
        }
        registerViewModel.verifyResult.observe(this@RegisterActivity, Observer {
            val verifyResult = it ?: return@Observer
            loading.visibility = View.GONE
            if (verifyResult.error != null) {
                showVerifyFailed(verifyResult.error)
            }
            if (verifyResult.success != null) {
                sendSuccessfully()
            }
            setResult(Activity.RESULT_OK)
            //Complete and destroy login activity once successful
        })
        registerViewModel.registerResult.observe(this@RegisterActivity, Observer {
            val registerResult = it ?: return@Observer
            loading.visibility = View.GONE
            if (registerResult.error != null) {
                showVerifyFailed(registerResult.error)
            }
            if (registerResult.success != null) {
                registerSuccessfully()
                intent = Intent(this, LoginActivity::class.java)
                startActivity(intent)
                finish()
            }
            setResult(Activity.RESULT_OK)
            //Complete and destroy login activity once successful
        })

    }
    private fun sendSuccessfully() {
        val welcome = "发送成功"
        Toast.makeText(
            applicationContext,
            welcome,
            Toast.LENGTH_LONG
        ).show()
    }

    private fun registerSuccessfully() {
        val welcome = "注册成功"
        Toast.makeText(
            applicationContext,
            welcome,
            Toast.LENGTH_LONG
        ).show()
    }

    //登录失败后的反应
    private fun showVerifyFailed(errorString: String) {
        Toast.makeText(applicationContext, errorString, Toast.LENGTH_SHORT).show()
    }
}
