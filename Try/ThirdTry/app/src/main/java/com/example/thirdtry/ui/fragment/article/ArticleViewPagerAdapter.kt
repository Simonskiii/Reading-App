package com.example.thirdtry.ui.fragment.article

import android.content.Context
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentPagerAdapter
import com.example.thirdtry.R
import com.example.thirdtry.ui.fragment.article.subfragment.ArticleSubFragment
import com.example.thirdtry.ui.fragment.scheme.subFragment.CommoditiesFragment
import com.example.thirdtry.ui.fragment.scheme.subFragment.TipsFragment

class ArticleViewPagerAdapter(
    private val context: Context,
    fragmentManager: FragmentManager
) : FragmentPagerAdapter(
    fragmentManager,
    BEHAVIOR_RESUME_ONLY_CURRENT_FRAGMENT
) {
    enum class SubFragments(val titleRes: String) {
        RECOMMEND("推荐"),
        SQZ("湿气重"),
        LITTLEHAIR("脱发"),
        POORSLEEP("失眠"),
        LOW_DKL("免疫力低下")
    }
    override fun getCount(): Int = SubFragments.values().size

    private fun getItemType(position: Int): SubFragments {
        return SubFragments.values()[position]
    }

    override fun getPageTitle(position: Int): CharSequence? {
        return getItemType(position).titleRes
    }

    override fun getItem(position: Int): Fragment {
        return when (getItemType(position)) {
            SubFragments.RECOMMEND -> ArticleSubFragment.newInstance(0)
            SubFragments.SQZ -> ArticleSubFragment.newInstance(1)
            SubFragments.LITTLEHAIR -> ArticleSubFragment.newInstance(2)
            SubFragments.POORSLEEP -> ArticleSubFragment.newInstance(3)
            SubFragments.LOW_DKL -> ArticleSubFragment.newInstance(4)
        }
    }
}