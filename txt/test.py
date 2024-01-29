import re
from openpyxl import Workbook

# 这是您提供的文本
text = """
export default {
  route: {
    errorPages: '错误页面',
    page401: '401',
    page404: '404',
    errorLog: '错误日志',
    theme: '换肤',
    clipboardDemo: 'Clipboard',
    i18n: '国际化',
    externalLink: '外链',
    profile: '个人中心',
    dashboard: '首页',
    TGchannelscall: 'Telegram频道净值',
    instructionForUse: '使用说明文档',
    aboutUs: '关于我们',
    SumbitTg: '收录TG频道',
    winnerChicken: '大吉大利，昨晚吃鸡',
    TGCalldetails: '频道喊单详细',
    tgAll: 'Telegram频道列表'
  },
  navbar: {
    dashboard: '首页',
    github: '项目地址',
    logOut: '退出登录',
    profile: '个人中心',
    theme: '换肤',
    size: '布局大小'
  },
  login: {
    title: '系统登录',
    logIn: '登录',
    username: '账号',
    password: '密码',
    any: '随便填',
    thirdparty: '第三方登录',
    thirdpartyTips: '本地不能模拟，请结合自己业务进行模拟！！！'
  },
  permission: {
    addRole: '新增角色',
    editPermission: '编辑权限',
    roles: '你的权限',
    switchRoles: '切换权限',
    tips: '在某些情况下，不适合使用 v-permission。例如：Element-UI 的 el-tab 或 el-table-column 以及其它动态渲染 dom 的场景。你只能通过手动设置 v-if 来实现。',
    delete: '删除',
    confirm: '确定',
    cancel: '取消'
  },
  chiken: {
    callTop: '昨日喊单',
    channelId: 'ID',
    tgName: 'TG频道名称',
    tokenName: 'Token 名称',
    tokenCA: 'Token 地址',
    callTime: '喊单时间',
    maxUpRate: '喊单后最高涨幅'
  },
  table: {
    title: 'TG频道链接',
    sellTime: '喊单后卖出的时间',
    time: '卖出时间',
    type: '类型',
    remark: '点评',
    search: '搜索',
    add: '添加',
    export: '导出',
    reviewer: '审核人',
    id: '序号',
    date: '时间',
    author: '作者',
    readings: '阅读数',
    status: '状态',
    actions: '操作',
    edit: '编辑',
    publish: '发布',
    draft: '草稿',
    delete: '删除',
    cancel: '取 消',
    confirm: '确 定',
    dataUpdateTime: '数据更新时间',
    numberTGchannels: '订阅TG频道数',
    channelId: 'ID',
    chat_id: '频道 ID',
    userName: '频道名称',
    net_value: '累计净值',
    members_count: '订阅人数',
    total_calls: '总喊单数',
    win_rate: '喊单胜率',
    nav_rate_7day: '近7天',
    nav_rate_1month: '近1月',
    nav_rate_3month: '近3月',
    nav_rate_6month: '近6月',
    nav_rate_1year: '近1年',
    nav_rate_all: '成立来',
    roi_mins_30: '30min后涨幅',
    roi_hours_1: '1hour后涨幅',
    roi_hours_2: '2hour后涨幅',
    roi_hours_4: '4hour后涨幅',
    roi_hours_6: '6hour后涨幅',
    roi_hours_12: '12hour后涨幅',
    roi_hours_24: '24hour后涨幅',
    nav_30min: '30分钟净值',
    nav_1hour: '1小时净值',
    nav_2hour: '2小时净值',
    nav_4hour: '4小时净值',
    nav_6hour: '6小时净值',
    nav_12hour: '12小时净值',
    nav_24hour: '24小时净值',
    day_to_call: '喊单天数',
    call_rate: '喊单频率',
    avg_rate: '喊单后价格变化中位数',
    max_up_total_rate: '最赚token盈利占比',
    medium_market_cap: '市值中位数',
    medium_entry_time: '入场时间中位数',
    medium_tvl: 'TVL中位数',
    message: '您搜索的telegram频道暂未收录，请点击下方按钮，我们会尽快收录，谢谢！',
    tgdata: '您搜索的telegram频道已收录，但我们暂时还没有订阅，有疑问请联系管理员，谢谢！',
    tgmessage: '此频道暂未订阅 !',
    tgwarning: '提示',
    submit: '提交收录',
    channel_details: '查看频道详细',
    match: '你已经成功匹配频道',
    call_price: '喊单价格/开盘价',
    market_cap: '市值(USD)',
    tvl: '流动性(USD)',
    mc_tvl: '市值/流动性',
    entry_time: '入场时间(分钟)',
    call_channel: '订阅频道',
    first_call: '首次喊单时间',
    mediumMC: '市值中位数',
    mediumTvl: '流动性中位数',
    mediumEntryTime: '入场时间中位数',
    is_subscribe: '是否订阅',
    all: '全部',
    yes: '是',
    no: '否',
    memberMessage: '频道的订阅人数',
    totalMessage: '频道自2023年1月1日以来的总喊单次数',
    dayMessage: '频道自2023年1月1日以来的总喊单天数',
    rateMessage: '频道每天的喊单次数 = 总喊单次数/总喊单天数',
    min30Message: '喊单后持仓30分钟卖出，计算频道净值',
    h1Message: '喊单后持仓1小时卖出，计算频道净值',
    h2Message: '喊单后持仓2小时卖出，计算频道净值',
    h4Message: '喊单后持仓4小时卖出，计算频道净值',
    h6Message: '喊单后持仓6小时卖出，计算频道净值',
    h12Message: '喊单后持仓12小时卖出，计算频道净值',
    h24Message: '喊单后持仓24小时卖出，计算频道净值',
    filter: '过滤器',
    reset: '重置'
  },
  settings: {
    title: '系统布局配置',
    theme: '主题色',
    tagsView: '开启 Tags-View',
    fixedHeader: '固定 Header',
    sidebarLogo: '侧边栏 Logo'
  },
  subLink: {
    link: '电报链接',
    submit: '提交',
    confirm: '确定',
    cancel: '取消',
    capatcha: '验证码',
    error: '温馨提示',
    success: '录入成功',
    successMessage: '录入成功,我们将尽快分析',
    error_400: '信息格式不是https://t.me/xxx',
    error_401: '请求过于频繁',
    error_402: '每人每天最多录入10个',
    error_403: '已关注过，频道质量太差',
    error_404: '频道已收录，是否跳转到详情页面？',
    error_405: '验证码有误',
    error_406: '请登录',
    error_407: '链接异常',
    error_604: '网络繁忙请稍后重试',
    check_from: '请检查表单内容',
    description: '请输入您想收录的telegram频道链接'
  },
  channel: {
    details: '频道详细'
  }
}
"""

# 使用正则表达式提取所有单引号和双引号内的文本
matches = re.findall(r"['\"](.*?)['\"]", text)

# 创建一个新的Excel工作簿
wb = Workbook()
ws = wb.active

# 将提取的文本添加到Excel工作表中
for match in matches:
    ws.append([match])

# 保存工作簿
wb.save("zh.xlsx")