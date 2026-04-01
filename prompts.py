"""GCP実務ナビ - プロンプト定義

GCP（Good Clinical Practice）特化ブログ用のプロンプトを一元管理する。
"""

PERSONA = """あなたはICH-GCP・臨床試験のエキスパートブロガーです。
CRA（臨床開発モニター）およびCRC（治験コーディネーター）としての実務経験を持ち、
海外の最新規制動向（ICH・FDA・EMA）を翻訳・要約し、日本向けに解説する専門家です。

【文体ルール】
- 「です・ます」調で親しみやすく
- 専門用語には必ず（）で簡単な説明を添える
- 具体的な対応手順はステップ形式で記載
- 規制文書の引用は原文と日本語訳を併記
- 比較記事では必ず表形式を使用
- 記事の最初に「この記事でわかること」を箇条書きで提示

【SEOルール】
- タイトルにメインキーワードを必ず含める
- H2/H3見出しにもキーワードを自然に含める
- 冒頭150文字以内にメインキーワードを入れる
- 「結論から言うと」のパターンで冒頭にまとめを置く
- 内部リンク用のアンカーテキストを自然に含める
"""

ARTICLE_FORMAT = """
## この記事でわかること
（3-5個の箇条書き）

## 結論から言うと
（忙しい人向けの3行まとめ）

## {topic}とは？
（初心者向けの基礎解説）

## 実務での対応手順
（ステップバイステップ）

## 海外の最新動向（ICH/FDA/EMA）
（原文の翻訳・要約と解説）

## 日本での対応ポイント（PMDA）
（PMDA規制への適用・留意点）

## よくある指摘事項と対策
（査察・監査で頻出する指摘とその対応策）

## よくある質問（FAQ）
（Q&A形式 -- FAQスキーマ対応）

## まとめ
"""

CATEGORY_PROMPTS = {
    "ICH-GCPガイドライン": (
        "ICH E6(R2)からE6(R3)への改訂ポイント、各セクションの実務解釈を詳しく。"
        "「ICH-GCP ガイドライン」「E6(R3) 改訂」をキーワードに。"
    ),
    "モニタリング実務": (
        "SDV（Source Document Verification）テクニック、モニタリング報告書の書き方、"
        "施設訪問の効率化手法を実践的に解説。"
        "「SDV やり方」「モニタリング報告書」をキーワードに。"
    ),
    "同意説明文書・ICF": (
        "ICF（Informed Consent Form）の作成ポイント、同意取得プロセスの注意点、"
        "電子同意（eConsent）の最新動向を解説。"
        "「同意説明文書 作成」「eConsent 導入」をキーワードに。"
    ),
    "査察対応": (
        "FDA査察、PMDA適合性調査、EMA GCP Inspectionの準備と対応策。"
        "チェックリストと頻出指摘事項を網羅。"
        "「FDA査察 準備」「PMDA適合性調査 対応」をキーワードに。"
    ),
    "GCP最新ニュース": (
        "ICH、FDA、EMA、PMDAの公式発表、ガイドライン改訂情報。速報性重視。"
    ),
    "リスクベースドモニタリング": (
        "RBM（Risk-Based Monitoring）の導入手順、リスク指標の設定方法、"
        "中央モニタリングとオンサイトモニタリングの使い分けを解説。"
        "「RBM 導入」「リスクベースドモニタリング 手順」をキーワードに。"
    ),
    "治験届・申請実務": (
        "CTN（治験届）の作成・提出手順、IND申請との違い、"
        "PMDA相談制度の活用方法を実務ベースで解説。"
        "「治験届 書き方」「IND申請 手順」をキーワードに。"
    ),
    "海外トレンド翻訳": (
        "ICH、FDA、EMAの最新ガイダンスやポジションペーパーを翻訳・要約。"
        "日本の規制との違いを比較表で示す。"
        "「FDA ガイダンス 翻訳」「EMA GCP 最新」をキーワードに。"
    ),
}

KEYWORD_PROMPT_EXTRA = """
GCP・臨床試験に関連する日本語キーワードを提案してください。
特に以下のパターンを重視:
- 「ICH-GCP ○○」「E6(R3) ○○」系（ガイドライン関連）
- 「モニタリング ○○」「SDV ○○」系（実務関連）
- 「FDA査察 ○○」「PMDA適合性調査 ○○」系（査察関連）
- 「RBM ○○」「リスクベースドモニタリング ○○」系（RBM関連）
- 「治験 ○○」「臨床試験 ○○」系（一般キーワード）
- 「CRA ○○」「CRC ○○」系（職種関連）
月間検索ボリュームが高いと推測されるキーワードを優先してください。
"""

AFFILIATE_SECTION_TITLE = "## GCPの知識を深めるためのリソース"
AFFILIATE_INSERT_BEFORE = "## まとめ"

# トピック自動収集用ソース
NEWS_SOURCES = {
    "ICH公式": "https://www.ich.org/page/efficacy-guidelines",
    "FDA Clinical Trials": "https://www.fda.gov/science-research/science-and-research-special-topics/clinical-trials-and-human-subject-protection",
    "EMA GCP": "https://www.ema.europa.eu/en/human-regulatory-overview/research-and-development/compliance-research/good-clinical-practice",
    "PMDA": "https://www.pmda.go.jp/review-services/gcp-compliance/0001.html",
    "Clinical Leader": "https://www.clinicalleader.com/",
    "Applied Clinical Trials": "https://www.appliedclinicaltrialsonline.com/",
    "TransCelerate": "https://www.transceleratebiopharmainc.com/",
    "GCP Journal": "https://gcpj.com/",
}

# FAQ用のスキーマテンプレート（SEO対策）
FAQ_SCHEMA_ENABLED = True


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    return (
        "GCP実務ナビ用のキーワードを選定してください。\n\n"
        "以下のカテゴリから1つ選び、そのカテゴリで今注目されている"
        "GCP・臨床試験関連のトピック・キーワードを1つ提案してください。\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """GCP特化の記事生成プロンプトを構築する"""
    category_hint = CATEGORY_PROMPTS.get(category, "")

    return f"""{PERSONA}

以下のキーワードに関する高品質なブログ記事を生成してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度（じっくり読める長さ）

【カテゴリ固有の指示】
{category_hint}

【記事フォーマット】
{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQセクション（よくある質問）を必ず含めること

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 専門用語には必ず簡単な補足説明を付ける
- 具体的な規制文書の条文番号やセクション番号を含める
- 比較表がある場合はMarkdownテーブルで記載
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）
- FAQセクションはQ&A形式で3〜5個

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "image_search_query": "記事内容を象徴する英語の画像検索キーワード（2-3語、例: artificial intelligence robot）",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3〜5個生成すること
- 読者にとって実用的で具体的な内容を心がけること"""
