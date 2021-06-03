def generate_all_euro_seasons(min_year=1993,max_year=2021):
    import numpy as np
    return [str(year) + "-" + str(year+1) for year in np.arange(min_year,max_year)]

def calc_outcome_FT_MatchResult1(FTHG,FTAG):
    if FTHG>FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResultX(FTHG,FTAG):
    if FTHG==FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult2(FTHG,FTAG):
    if FTHG<FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult1(HTHG,HTAG):
    if HTHG>HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResultX(HTHG,HTAG):
    if HTHG==HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult2(HTHG,HTAG):
    if HTHG<HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResult11(HTHG,HTAG,FTHG,FTAG):
    if HTHG>HTAG and FTHG>FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResult1X(HTHG,HTAG,FTHG,FTAG):
    if HTHG>HTAG and FTHG==FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResult12(HTHG,HTAG,FTHG,FTAG):
    if HTHG>HTAG and FTHG<FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResultX1(HTHG,HTAG,FTHG,FTAG):
    if HTHG==HTAG and FTHG>FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResultXX(HTHG,HTAG,FTHG,FTAG):
    if HTHG==HTAG and FTHG==FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResultX2(HTHG,HTAG,FTHG,FTAG):
    if HTHG==HTAG and FTHG<FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResult21(HTHG,HTAG,FTHG,FTAG):
    if HTHG<HTAG and FTHG>FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResult2X(HTHG,HTAG,FTHG,FTAG):
    if HTHG<HTAG and FTHG==FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HTFT_MatchResult22(HTHG,HTAG,FTHG,FTAG):
    if HTHG<HTAG and FTHG<FTAG :
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult1_handicap10(HTHG,HTAG):
    if 1+HTHG>HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResultX_handicap10(HTHG,HTAG):
    if 1+HTHG==HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult2_handicap10(HTHG,HTAG):
    if 1+HTHG<HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult1_handicap10(FTHG,FTAG):
    if 1+FTHG>FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResultX_handicap10(FTHG,FTAG):
    if 1+FTHG==FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult2_handicap10(FTHG,FTAG):
    if 1+FTHG<FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult1_handicap20(HTHG,HTAG):
    if 2+HTHG>HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResultX_handicap20(HTHG,HTAG):
    if 2+HTHG==HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult2_handicap20(HTHG,HTAG):
    if 2+HTHG<HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult1_handicap20(FTHG,FTAG):
    if 2+FTHG>FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResultX_handicap20(FTHG,FTAG):
    if 2+FTHG==FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult2_handicap20(FTHG,FTAG):
    if 2+FTHG<FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult1_handicap01(HTHG,HTAG):
    if -1+HTHG>HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResultX_handicap01(HTHG,HTAG):
    if -1+HTHG==HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult2_handicap01(HTHG,HTAG):
    if -1+HTHG<HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult1_handicap01(FTHG,FTAG):
    if -1+FTHG>FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResultX_handicap01(FTHG,FTAG):
    if -1+FTHG==FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult2_handicap01(FTHG,FTAG):
    if -1+FTHG<FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult1_handicap02(HTHG,HTAG):
    if -2+HTHG>HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResultX_handicap02(HTHG,HTAG):
    if -2+HTHG==HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_MatchResult2_handicap02(HTHG,HTAG):
    if -2+HTHG<HTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult1_handicap02(FTHG,FTAG):
    if -2+FTHG>FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResultX_handicap02(FTHG,FTAG):
    if -2+FTHG==FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_MatchResult2_handicap02(FTHG,FTAG):
    if -2+FTHG<FTAG:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_OverUnder05(HTHG,HTAG):
    if HTHG+HTAG>0.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_OverUnder15(HTHG,HTAG):
    if HTHG+HTAG>1.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_OverUnder25(HTHG,HTAG):
    if HTHG+HTAG>2.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_HT_OverUnder35(HTHG,HTAG):
    if HTHG+HTAG>3.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder05(FTHG,FTAG):
    if FTHG+FTAG>0.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder15(FTHG,FTAG):
    if FTHG+FTAG>1.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder25(FTHG,FTAG):
    if FTHG+FTAG>2.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder35(FTHG,FTAG):
    if FTHG+FTAG>3.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder45(FTHG,FTAG):
    if FTHG+FTAG>3.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder55(FTHG,FTAG):
    if FTHG+FTAG>3.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder65(FTHG,FTAG):
    if FTHG+FTAG>3.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_OverUnder75(FTHG,FTAG):
    if FTHG+FTAG>3.5:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_EqualUnequal(FTHG,FTAG):
    if FTHG+FTAG%2==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_BothTeamsScore(FTHG,FTAG):
    if FTHG>0 and FTAG>0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiff4(FTHG,FTAG):
    if abs(FTHG-FTAG)==4:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiff3(FTHG,FTAG):
    if abs(FTHG-FTAG)==3:
        return "Yes"
    else:
        return "No"
        
def calc_outcome_FT_GoalDiff2(FTHG,FTAG):
    if abs(FTHG-FTAG)==2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiff1(FTHG,FTAG):
    if abs(FTHG-FTAG)==1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiff0(FTHG,FTAG):
    if abs(FTHG-FTAG)==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAwayMinus4(FTHG,FTAG):
    if FTHG-FTAG<=-4:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAwayMinus3(FTHG,FTAG):
    if FTHG-FTAG==-3:
        return "Yes"
    else:
        return "No"
        
def calc_outcome_FT_GoalDiffHomeAwayMinus2(FTHG,FTAG):
    if FTHG-FTAG==-2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAwayMinus1(FTHG,FTAG):
    if FTHG-FTAG==-1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAway0(FTHG,FTAG):
    if FTHG-FTAG==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAwayPlus1(FTHG,FTAG):
    if FTHG-FTAG==1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAwayPlus2(FTHG,FTAG):
    if FTHG-FTAG==2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAwayPlus3(FTHG,FTAG):
    if FTHG-FTAG==3:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_GoalDiffHomeAwayMoreThan4(FTHG,FTAG):
    if FTHG-FTAG>=4:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_00(FTHG,FTAG):
    if FTHG==0 and FTAG==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_11(FTHG,FTAG):
    if FTHG==1 and FTAG==1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_22(FTHG,FTAG):
    if FTHG==2 and FTAG==2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_33(FTHG,FTAG):
    if FTHG==3 and FTAG==3:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_44(FTHG,FTAG):
    if FTHG==4 and FTAG==4:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_10(FTHG,FTAG):
    if FTHG==1 and FTAG==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_20(FTHG,FTAG):
    if FTHG==2 and FTAG==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_30(FTHG,FTAG):
    if FTHG==3 and FTAG==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_40(FTHG,FTAG):
    if FTHG==4 and FTAG==0:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_21(FTHG,FTAG):
    if FTHG==2 and FTAG==1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_31(FTHG,FTAG):
    if FTHG==3 and FTAG==1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_41(FTHG,FTAG):
    if FTHG==4 and FTAG==1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_32(FTHG,FTAG):
    if FTHG==3 and FTAG==2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_42(FTHG,FTAG):
    if FTHG==4 and FTAG==2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_43(FTHG,FTAG):
    if FTHG==4 and FTAG==3:
        return "Yes"
    else:
        return "No"


def calc_outcome_FT_Score_01(FTHG,FTAG):
    if FTHG==0 and FTAG==1:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_02(FTHG,FTAG):
    if FTHG==0 and FTAG==2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_03(FTHG,FTAG):
    if FTHG==0 and FTAG==3:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_04(FTHG,FTAG):
    if FTHG==0 and FTAG==4:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_12(FTHG,FTAG):
    if FTHG==1 and FTAG==2:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_13(FTHG,FTAG):
    if FTHG==1 and FTAG==3:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_14(FTHG,FTAG):
    if FTHG==1 and FTAG==4:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_23(FTHG,FTAG):
    if FTHG==2 and FTAG==3:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_24(FTHG,FTAG):
    if FTHG==2 and FTAG==4:
        return "Yes"
    else:
        return "No"

def calc_outcome_FT_Score_34(FTHG,FTAG):
    if FTHG==3 and FTAG==4:
        return "Yes"
    else:
        return "No"
