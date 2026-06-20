window.HSO_GRAPH = {
  nodes: [
    { id: "sleep", label: "睡眠", type: "module", detail: "健康、学习、代谢和情绪的基础。" },
    { id: "diet", label: "饮食/禁食", type: "module", detail: "进食窗口、血糖状态、肠道菌群和饮食结构。" },
    { id: "dopamine", label: "多巴胺", type: "mechanism", detail: "动机、奖励、快乐阈值和专注协调。" },
    { id: "focus", label: "学习专注", type: "module", detail: "犯错信号、神经可塑性、休息和注意力环境。" },
    { id: "brain", label: "大脑健康", type: "module", detail: "有氧运动、Omega-3、胆碱、电解质。" },
    { id: "longevity", label: "长寿", type: "module", detail: "饮食、运动、监测、药物争议和细胞重编程。" },
    { id: "practice", label: "个人实践", type: "module", detail: "把知识转成低摩擦日常习惯。" },
    { id: "light", label: "晨间光照", type: "practice", detail: "起床后户外 2-10 分钟。" },
    { id: "night_light", label: "夜间避光", type: "practice", detail: "尤其避免 23:00-04:00 强光。" },
    { id: "fasting", label: "进食窗口", type: "practice", detail: "基础版睡前 2-3 小时不吃，高阶 8 小时窗口。" },
    { id: "fermented", label: "发酵食品", type: "practice", detail: "每天两次自然发酵食品，支持菌群多样性。" },
    { id: "exercise", label: "有氧+力量", type: "practice", detail: "每周约 150-180 分钟有氧，搭配力量训练。" },
    { id: "nsdr", label: "NSDR/冥想", type: "practice", detail: "午休、Yoga Nidra、生理叹息和深度休息。" },
    { id: "caution_drugs", label: "药物/补剂争议", type: "risk", detail: "NMN、白藜芦醇、二甲双胍、聪明药等需谨慎。" },
    { id: "medical", label: "医学边界", type: "risk", detail: "药物、慢病、异常指标、极端禁食需要专业意见。" }
  ],
  edges: [
    { source: "light", target: "sleep", relation: "校准昼夜节律" },
    { source: "night_light", target: "sleep", relation: "降低节律扰动" },
    { source: "sleep", target: "dopamine", relation: "夜间光照影响后续多巴胺状态" },
    { source: "dopamine", target: "focus", relation: "支持动机和专注网络协调" },
    { source: "sleep", target: "focus", relation: "睡眠中巩固学习" },
    { source: "nsdr", target: "focus", relation: "降低压力并支持学习恢复" },
    { source: "fasting", target: "diet", relation: "控制进食时间和血糖状态" },
    { source: "fermented", target: "diet", relation: "提升肠道菌群多样性" },
    { source: "exercise", target: "brain", relation: "有氧支持大脑供能" },
    { source: "exercise", target: "longevity", relation: "心肺和肌肉能力支持延寿" },
    { source: "diet", target: "longevity", relation: "饮食结构和禁食影响衰老机制" },
    { source: "practice", target: "sleep", relation: "晨光和夜间避光可训练" },
    { source: "practice", target: "diet", relation: "进食窗口可训练" },
    { source: "practice", target: "focus", relation: "专注块和阅读可训练" },
    { source: "caution_drugs", target: "longevity", relation: "抗衰药物证据争议" },
    { source: "medical", target: "caution_drugs", relation: "涉及药物和异常指标需专业意见" },
    { source: "medical", target: "fasting", relation: "极端禁食需专业评估" }
  ]
};
