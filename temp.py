class Capacitor:

    Cap_Type = ""
    Working_temprature = 30
    Enviroment_Type = "GB"
    Capacity = ""
    def __uF(self,cap_value):
        return cap_value * (10**6)
    def __pF(self,cap_value):
        return cap_value
    def __nF(self,cap_value):
        return cap_value *(10**3)
    def __F(self,cap_value):
        return cap_value *(10**12)

    package_coefficient = {"1st_Class_Ceramic_Chip_capacitors": 1.5, "一类陶瓷电容_有引线": 1.0,
                        "2nd_Class_Ceramic_Chip_capacitors": 1.5, "二类陶瓷电容_有引线": 1.0,
                        "3rd_Class_Ceramic_Chip_capacitors": 1.5, "三类陶瓷电容_有引线": 1.0,
                        "Tantalum_capacitors_Chip": 1.2, "固体钽电解电容_有引线": 1.0,
                        "Aluminum_capacitors_Chip": 1.2, "铝电解电容_有引线": 1.0,
                        "Film_capacitors_Chip": 1.2, "薄膜电容_有引线": 1.0}

    一类陶瓷电容环境系数 = {"GB": 1.0,"GMS": 1.2, "GF1": 2.4, "GF2": 4.1, "GM1": 4.6, "GM2": 7.6,
                        "MP": 7.0, "NSB": 4.0, "NS1": 2.3, "NS2": 4.7, "NU": 10.2, "AIF": 6.7,
                        "AUF": 12, "AIC": 3.4, "AUC": 7.5, "ARW": 10.5, "SF": 1.0, "ML": 17,
                        "MF": 8}
    一类陶瓷电容基本失效率 = {0: 0.0030, 5: 0.0035, 10: 0.0041, 15: 0.0048, 20: 0.0056, 25: 0.0066, 30: 0.0077,
                          35: 0.0089, 40: 0.0104, 45: 0.0121, 50: 0.1401, 55: 0.0165, 60: 0.0192, 65: 0.0224,
                          70: 0.0261, 75: 0.0305, 80: 0.0356, 85: 0.0415
                          }  # 基于S = 0.5 条件下进行计算所得到的数据
    一类陶瓷电容质量等级 = {"A1P": 0.03, "A1M": 0.1, "A2": 0.3, "B1": 0.5, "B2": 1, "C": 5
                        }
    一类陶瓷电容容量系数 = {"小于7.5pF": 0.50, "7.5pF到91pF": 0.75, "91pF到470pF": 1.0, "470pF到2000pF": 1.3,
                            "2000pF到0.0062uF": 1.6, "0.0062uF到0.016uF": 1.9, "0.016uF到0.039uF": 2.2,
                            "大于0.039uF": 2.4}
    def __解析一类陶瓷电容容量系数(self,电容值):
        绝对电容值 = self.__解析电容值(电容值)
        if 绝对电容值 < 7.5:
            self.Capacity = "小于7.5pF"
            self.容量系数 = 0.5
        elif 绝对电容值>= 7.5 and 绝对电容值 < 91:
            self.容量系数 = 0.75
        elif 绝对电容值 >= 91 and 绝对电容值 < 470:
            self.容量系数 = 1.0
        elif 绝对电容值 >= 470 and 绝对电容值<2000:
            self.容量系数 = 1.3
        elif 绝对电容值 >= 2000 and 绝对电容值 < 6200:
            self.容量系数 = 1.6
        elif 绝对电容值 >= 6200 and 绝对电容值 < 16000:
            self.容量系数 = 1.9
        elif 绝对电容值 >= 16000 and 绝对电容值 < 39000:
            self.容量系数 = 2.2
        elif 绝对电容值 >= 39000:
            self.容量系数 = 2.4
    二类陶瓷电容环境系数 = {"GB": 1.0, "GMS": 1.2, "GF1": 2.8, "GF2": 4.6, "GM1": 5.1, "GM2": 8.1, "MP": 7.0, "NSB": 4.9,
                            "NS1": 2.9, "NS2": 5.7, "NU": 9.1, "AIF": 7.7, "AUF": 14, "AIC": 6.0, "AUC": 10.2,
                            "ARW": 12, "SF": 1.0, "ML": 17, "MF": 8}
    二类陶瓷电容基本失效率 = {0: 0.00748, 5: 0.00759, 10: 0.00769, 15: 0.00780, 20: 0.00791, 25: 0.00802, 30: 0.00814,
                              35: 0.00825, 40: 0.00837, 45: 0.00848, 50: 0.00860, 55: 0.00873, 60: 0.00885, 65: 0.00897,
                              70: 0.00910, 75: 0.00923, 80: 0.00936, 85: 0.00949
                              }  # 基于S = 0.5 条件下进行计算所得到的数据
    二类陶瓷电容质量等级 = {"A1P": 0.03, "A1M": 0.1, "A2": 0.3, "B1": 0.5, "B2": 1, "C": 5
                  }
    二类陶瓷电容容量系数 = {"小于240pF": 0.50, "240pF到0.0033uF": 0.75, "0.0033uF到0.016uF": 1.0,
                            "0.016uF到0.082uF": 1.3, "0.082uF到0.27uF": 1.6, "0.27uF到0.75uF": 1.9,
                            "0.75uF到1.8uF": 2.2, "大于1.8uF": 2.4}
    def __解析二类陶瓷电容容量系数(self, 电容值):
        绝对电容值 = self.__解析电容值(电容值)
        if 绝对电容值 <= 240:
            self.容量系数 = 0.50
        elif 绝对电容值 > 240 and 绝对电容值 <= 3300:
            self.容量系数 = 0.75
        elif 绝对电容值 > 3300 and 绝对电容值 <= 16000:
            self.容量系数 = 1.0
        elif 绝对电容值 > 16000 and 绝对电容值 <= 82000:
            self.容量系数 = 1.3
        elif 绝对电容值 > 82000 and 绝对电容值 <= 270000:
            self.容量系数 = 1.6
        elif 绝对电容值 > 270000 and 绝对电容值 <= 750000:
            self.容量系数 = 1.9
        elif 绝对电容值 > 750000 and 绝对电容值 <= 1800000:
            self.容量系数 = 2.2
        elif 绝对电容值 > 1800000:
            self.容量系数 = 2.4


    三类陶瓷电容环境系数 = {"GB": 1.0, "GMS": 1.2, "GF1": 2.4, "GF2": 4.8, "GM1": 4.85, "GM2": 7.9, "MP": 7.0, "NSB": 4.9,
                            "NS1": 2.6, "NS2": 5.0, "NU": 9.6, "AIF": 7.2, "AUF": 13, "AIC": 4.4, "AUC": 8.7,
                            "ARW": 11, "SF": 1.0, "ML": 17, "MF": 8.0}
    三类陶瓷电容基本失效率 = {0: 0.0045, 5: 0.0049, 10: 0.0054, 15: 0.0060, 20: 0.0066, 25: 0.0073, 30: 0.0080,
                              35: 0.0088, 40: 0.0097, 45: 0.0107, 50: 0.0118, 55: 0.0130, 60: 0.0144, 65: 0.0159,
                              70: 0.0175, 75: 0.0193, 80: 0.0213, 85: 0.0235
                              }  # 基于S = 0.5 条件下进行计算所得到的数据
    三类陶瓷电容质量等级 = { "A": 0.3, "B1": 0.5, "B2": 1, "C": 5
                  }
    三类陶瓷电容容量系数 = {"小于50pF": 0.51, "50pF到240pF": 0.62, "240pF到0.0033uF": 0.85,
                            "0.0033uF到0.016uF": 1.00, "0.016uF到0.082uF": 1.24, "0.082uF到0.27uF": 1.44,
                            "0.27uF到0.75uF": 1.62,
                            "0.75uF到1.8uF": 1.80, "大于1.8uF": 2.20}
    def __解析三类陶瓷电容容量系数(self,电容值):
        绝对电容值 = self.__解析电容值(电容值)
        if 绝对电容值 <= 50:
            self.容量系数 = 0.51
        elif 绝对电容值 > 50 and 绝对电容值 <= 240:
            self.容量系数 = 0.62
        elif 绝对电容值 > 240 and 绝对电容值 <= 3300:
            self.容量系数 = 0.85
        elif 绝对电容值 > 3300 and 绝对电容值 <= 16000:
            self.容量系数 = 1.0
        elif 绝对电容值 > 16000 and 绝对电容值 <= 82000:
            self.容量系数 = 1.24
        elif 绝对电容值 > 82000 and 绝对电容值 <= 270000:
            self.容量系数 = 1.44
        elif 绝对电容值 > 270000 and 绝对电容值 <= 750000:
            self.容量系数 = 1.62
        elif 绝对电容值 > 750000 and 绝对电容值 <= 1800000:
            self.容量系数 = 1.80
        elif 绝对电容值 > 1800000:
            self.容量系数 = 2.20


    固体钽电解电容环境系数 = {"GB": 1.0, "GMS": 1.2, "GF1": 2.4, "GF2": 3.5, "GM1": 3.5, "GM2": 6.5, "MP": 6.0, "NSB":3.8,
                            "NS1": 2.3, "NS2": 4.5, "NU": 8.5, "AIF": 8.3, "AUF": 15, "AIC": 5.5, "AUC": 8.0,
                            "ARW": 12, "SF": 1.0, "ML": 19, "MF": 9}
    固体钽电解电容基本失效率 = {0: 0.0085, 5: 0.0089, 10: 0.0093, 15: 0.0098, 20: 0.0104, 25: 0.0112, 30: 0.0121,
                                35: 0.0133, 40: 0.0148, 45: 0.0166, 50: 0.0190, 55: 0.0222, 60: 0.0263, 65: 0.0320,
                                70: 0.0398, 75: 0.0509, 80: 0.0671, 85: 0.0914, 90: 0.1292, 95: 0.1901,100: 0.2923,
                                105: 0.4718
                              }  # 基于S = 0.5 条件下进行计算所得到的数据
    固体钽电解电容质量等级 = {"A1P": 0.03,"A1M": 0.1, "A2": 0.3, "B1": 0.5, "B2": 1, "C": 5
                  }
    固体钽电解电容容量系数 = {"小于0.47uF": 0.50, "0.47uF到3.3uF": 0.75, "3.3uF到15uF": 1.0,
                            "15uF到47uF": 1.3, "47uF到100uF": 1.6, "100uF到220uF": 1.9,
                            "220uF到500uF": 2.2,
                            "大于500uF": 2.6}
    固体钽电解电容电阻系数 = {"大于3": 0.07, "2到3": 0.1, "1到2": 0.2, "0.8到1": 0.3, "0.6到0.8": 0.4, "0.4到0.6": 0.6,
                              "0.2到0.4": 0.8, "小于0.2": 1.0}
    def __解析固体钽电解电容容量系数(self,电容值):
        绝对电容值 = self.__解析电容值(电容值)
        if 绝对电容值 <= self.__uF(0.47):
            self.容量系数 = 0.50
        elif 绝对电容值 > self.__uF(0.47) and 绝对电容值 <= self.__uF(3.3):
            self.容量系数 = 0.75
        elif 绝对电容值 > self.__uF(3.3) and 绝对电容值 <= self.__uF(15):
            self.容量系数 = 1.0
        elif 绝对电容值 > self.__uF(15) and 绝对电容值 <= self.__uF(47):
            self.容量系数 = 1.3
        elif 绝对电容值 > self.__uF(47) and 绝对电容值 <= self.__uF(100):
            self.容量系数 = 1.6
        elif 绝对电容值 >self.__uF(100) and 绝对电容值 <= self.__uF(220):
            self.容量系数 = 1.9
        elif 绝对电容值 > self.__uF(220) and 绝对电容值 <= self.__uF(500):
            self.容量系数 = 2.2
        elif 绝对电容值 > self.__uF(500) :
            self.容量系数 = 2.6

    # 非固体钽电解电容器还未写
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    铝电解电容环境系数 = {  "GB": 1.0, "GMS": 1.2, "GF1": 2.4, "GF2": 4.0, "GM1": 4.2, "GM2": 10.4, "MP": 9.0, "NSB":5.1,
                            "NS1": 3.0, "NS2": 6.1, "NU": 12.7, "AIF": 11.8, "AUF": 21, "AIC": 9.0, "AUC": 15,
                            "ARW": 18, "SF": 1.0, "ML": 21, "MF": 10}
    铝电解电容基本失效率 = {0: 0.028, 5: 0.0308, 10: 0.0341, 15: 0.0381, 20: 0.0430, 25: 0.0490, 30: 0.0565,
                                35: 0.0660, 40: 0.0781, 45: 0.0936, 50: 0.1139, 55: 0.1407, 60: 0.1767, 65: 0.2258,
                                70: 0.2940, 75: 0.3902, 80: 0.5288, 85: 0.7324,
                            }  # 基于S = 0.5 条件下进行计算所得到的数据
    铝电解电容质量等级 = {"A1L": 0.03,"A1W": 0.1, "A2": 0.3, "B1": 0.5, "B2": 1, "C": 5
                  }
    铝电解电容容量系数 = {"小于1uF": 0.40, "1uF到20uF": 0.70, "20uF到100uF": 1.0,
                            "100uF到470uF": 1.3, "470uF到1500uF": 1.6, "1500uF到3000uF": 1.9,
                            "3000uF到6800uF": 2.2,"6800uF到10000uF":2.5, "10000uF到20000uF":2.8,
                            "大于20000uF": 3.0}
    def __解析铝电解电容容量系数(self,电容值):
        绝对电容值 = self.__解析电容值(电容值)
        if 绝对电容值 < self.__uF(1.0):
            self.容量系数 = 0.4
        elif self.__uF(1.0) <= 绝对电容值 < self.__uF(20):
            self.容量系数 = 0.7
        elif self.__uF(20) <= 绝对电容值 < self.__uF(100):
            self.容量系数 = 1.0
        elif self.__uF(100) <= 绝对电容值 < self.__uF(470):
            self.容量系数 = 1.3
        elif self.__uF(470) <= 绝对电容值 < self.__uF(1500):
            self.容量系数 = 1.6
        elif self.__uF(1500) <= 绝对电容值 < self.__uF(3000):
            self.容量系数 = 1.9
        elif self.__uF(3000) <= 绝对电容值 < self.__uF(6800):
            self.容量系数 = 2.2
        elif self.__uF(6800) <= 绝对电容值 < self.__uF(10000):
            self.容量系数 = 2.5
        elif self.__uF(10000) <= 绝对电容值 < self.__uF(20000):
            self.容量系数 = 2.8
        elif 绝对电容值>= self.__uF(20000):
            self.容量系数 = 3.0
    def _解析电容类型(self,电容类型):
        if re.search("一",str(电容类型)):
            self.Cap_Type  = "一类陶瓷电容"
        elif re.search("二",str(电容类型)):
            self.Cap_Type = "二类陶瓷电容"
        elif re.search("三",str(电容类型)):
            self.Cap_Type = "三类陶瓷电容"
        elif re.search("钽",str(电容类型)):
            self.Cap_Type = "固体钽电解电容"
        elif re.search("铝",str(电容类型)):
            self.Cap_Type = "铝电解电容"
    def __解析电容值(self,电容值):
        if re.search("u",str(电容值)) or re.search("U",str(电容值)):
            电容值解析结果 = int(re.match(r'\d+',电容值).group())* (10**6)
        elif (re.search("n",str(电容值)) or re.search("N",str(电容值))):
            电容值解析结果 = int(re.match(r'\d+', 电容值).group()) * (10**3)
        elif(re.search("p",str(电容值)) or re.search("P",str(电容值))):
            电容值解析结果 = int(re.match(r'\d+', 电容值).group())
        else:
            电容值解析结果 = int(re.match(r'\d+', 电容值).group())*(10**9)
        return 电容值解析结果



        pass
    def __得到容量系数(self,电容值):
        if self.Cap_Type == "一类陶瓷电容":
            self.__解析一类陶瓷电容容量系数(电容值)
        elif self.Cap_Type == "二类陶瓷电容":
            self.__解析二类陶瓷电容容量系数(电容值)
        elif self.Cap_Type == "三类陶瓷电容":
            self.__解析三类陶瓷电容容量系数(电容值)
        elif self.Cap_Type == "固体钽电解电容":
            self.__解析固体钽电解电容容量系数(电容值)
        elif self.Cap_Type == "铝电解电容":
            self.__解析铝电解电容容量系数(电容值)




    def 得到可靠性(self):
        if self.Cap_Type == "":
            print("设备未能正确初始化")
        elif self.Cap_Type == "固体钽电解电容":
            step1 = self.固体钽电解电容基本失效率[self.Working_temprature] / 1000000 * \
                    self.固体钽电解电容环境系数[self.Enviroment_Type]
            step2 = self.固体钽电解电容质量等级["B1"] * \
                    self.容量系数
            step3 = self.固体钽电解电容电阻系数["小于0.2"]* \
                    self.package_coefficient["Tantalum_capacitors_Chip"]
            step4 = step1 * step2 * step3

            return  step4
        elif self.Cap_Type == "一类陶瓷电容":
            step1 = self.一类陶瓷电容基本失效率[self.Working_temprature] / 1000000 * \
                    self.一类陶瓷电容环境系数[self.Enviroment_Type]
            step2 = self.一类陶瓷电容质量等级["A1P"] * \
                    self.容量系数
            step3 = step1 * step2 * self.package_coefficient["1st_Class_Ceramic_Chip_capacitors"]

            return  step3
        elif self.Cap_Type == "二类陶瓷电容":
            step1 = self.二类陶瓷电容基本失效率[self.Working_temprature] / 1000000 * \
                    self.二类陶瓷电容环境系数[self.Enviroment_Type]
            step2 = self.二类陶瓷电容质量等级["A1P"] * \
                    self.容量系数
            step3 = step1 * step2 * self.package_coefficient["2nd_Class_Ceramic_Chip_capacitors"]

            return step3
        elif self.Cap_Type == "三类陶瓷电容":
            step1 = self.三类陶瓷电容基本失效率[self.Working_temprature] / 1000000 * \
                    self.三类陶瓷电容环境系数[self.Enviroment_Type]
            step2 = self.三类陶瓷电容质量等级["A"] * \
                    self.容量系数
            step3 = step1 * step2 * self.package_coefficient["3rd_Class_Ceramic_Chip_capacitors"]

            return step3

        elif self.Cap_Type == "铝电解电容":

            step1 = self.铝电解电容基本失效率[self.Working_temprature] / 1000000 * \
                    self.铝电解电容环境系数[self.Enviroment_Type]
            step2 = self.铝电解电容质量等级["A1L"] * \
                    self.容量系数
            step3 = step1 * step2 * self.package_coefficient["Aluminum_capacitors_Chip"]

            return step3
        else:
            print("Pls confirm your capacitor's type")

    def __init__(self, 电容类型, 工作温度, 环境类型, 电容容量):
        self._解析电容类型(电容类型)
        self.Working_temprature = 工作温度
        self.Enviroment_Type = 环境类型
        self.__得到容量系数(电容容量)