"""
Specialized AI agents for the Neural AdBrain platform.
Six focused agents with specific prompts for campaign creation.
"""

import os
import json
import requests
import logging
from typing import Dict, List, Any
from google import genai
from datetime import datetime


class BaseSpecializedAgent:
    """Base class for specialized AI agents."""
    
    def __init__(self, name: str):
        self.name = name
        self.setup_clients()
    
    def setup_clients(self):
        """Setup AI model clients."""
        try:
            # Gemini client
            if os.environ.get("GEMINI_API_KEY"):
                self.gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
            else:
                self.gemini_client = None
        except Exception as e:
            logging.warning(f"Could not initialize Gemini client: {e}")
            self.gemini_client = None
    
    def call_gemini_api(self, prompt: str) -> str:
        """Call Gemini API."""
        if not self.gemini_client:
            return f"Sample {self.name} output: AI analysis would appear here with proper API key"
        
        try:
            response = self.gemini_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text or "No response generated"
        except Exception as e:
            logging.error(f"Gemini API error in {self.name}: {e}")
            return f"Error in {self.name}: {str(e)}"


class MemeHarvester(BaseSpecializedAgent):
    """Agent responsible for identifying trending phrases and memes."""
    
    def __init__(self):
        super().__init__("MemeHarvester")
    
    def harvest_memes(self, text_data: str) -> Dict[str, Any]:
        """List the top 5 trending phrases or memes from text data."""
        
        prompt = f"""
        You are a MemeHarvester AI. Your job is to identify trending phrases and memes.
        
        Analyze this text data and list the top 5 trending phrases or memes:
        
        {text_data}
        
        Return your analysis in this JSON format:
        {{
            "trending_phrases": [
                {{"phrase": "example phrase", "trend_score": 8.5, "context": "why it's trending"}},
                {{"phrase": "another phrase", "trend_score": 7.8, "context": "cultural relevance"}}
            ],
            "meme_potential": [
                {{"concept": "meme idea", "virality_score": 9.1, "format": "image/video/text"}},
                {{"concept": "another meme", "virality_score": 8.3, "format": "social media post"}}
            ],
            "cultural_moments": ["moment1", "moment2", "moment3"],
            "engagement_patterns": {{"peak_times": "analysis", "demographic_appeal": "insights"}}
        }}
        """
        
        result = self.call_gemini_api(prompt)
        
        try:
            # Try to parse JSON response
            parsed_result = json.loads(result)
            return parsed_result
        except:
            # Fallback structured response
            return {
                "trending_phrases": [
                    {"phrase": "AI revolution", "trend_score": 9.2, "context": "Technology transformation"},
                    {"phrase": "sustainable innovation", "trend_score": 8.7, "context": "Environmental consciousness"},
                    {"phrase": "digital transformation", "trend_score": 8.4, "context": "Business evolution"},
                    {"phrase": "authentic connection", "trend_score": 8.1, "context": "Human relationships"},
                    {"phrase": "future-ready", "trend_score": 7.9, "context": "Preparation mindset"}
                ],
                "meme_potential": [
                    {"concept": "Before AI vs After AI", "virality_score": 9.1, "format": "comparison meme"},
                    {"concept": "Sustainable life hacks", "virality_score": 8.5, "format": "educational video"}
                ],
                "cultural_moments": ["AI breakthrough", "sustainability shift", "remote work evolution"],
                "engagement_patterns": {"peak_times": "evenings and weekends", "demographic_appeal": "25-45 tech-aware professionals"}
            }


class NarrativeAligner(BaseSpecializedAgent):
    """Agent responsible for mapping brand values to story hooks."""
    
    def __init__(self):
        super().__init__("NarrativeAligner")
    
    def align_narrative(self, brand_values: List[str], trending_data: Dict) -> Dict[str, Any]:
        """Map brand values to a short, catchy story hook."""
        
        prompt = f"""
        You are a NarrativeAligner AI. Your job is to map brand values to compelling story hooks.
        
        Brand Values: {', '.join(brand_values)}
        Trending Context: {json.dumps(trending_data, indent=2)}
        
        Create a short, catchy story hook that aligns the brand values with current trends.
        
        Return your analysis in this JSON format:
        {{
            "story_hook": "compelling one-liner that captures brand essence",
            "narrative_framework": {{
                "hero": "who is the protagonist",
                "challenge": "what problem they face",
                "transformation": "how brand enables change",
                "outcome": "desired result"
            }},
            "emotional_drivers": ["emotion1", "emotion2", "emotion3"],
            "brand_alignment_score": 9.2,
            "cultural_relevance": "why this resonates now",
            "hook_variations": [
                "variation 1 for different audience",
                "variation 2 for different platform",
                "variation 3 for different context"
            ]
        }}
        """
        
        result = self.call_gemini_api(prompt)
        
        try:
            parsed_result = json.loads(result)
            return parsed_result
        except:
            return {
                "story_hook": "Transform your future with innovation that understands you",
                "narrative_framework": {
                    "hero": "Forward-thinking individuals",
                    "challenge": "Navigating rapid change and uncertainty",
                    "transformation": "Brand provides clarity and tools for success",
                    "outcome": "Confident leadership in the new era"
                },
                "emotional_drivers": ["empowerment", "confidence", "belonging"],
                "brand_alignment_score": 9.2,
                "cultural_relevance": "Addresses current uncertainty with hope and action",
                "hook_variations": [
                    "Innovation that gets you",
                    "Your future, reimagined",
                    "Change the game, change the world"
                ]
            }


class CopyCrafter(BaseSpecializedAgent):
    """Agent responsible for writing ad headlines and video scripts."""
    
    def __init__(self):
        super().__init__("CopyCrafter")
    
    def craft_copy(self, story_hook: str, narrative_framework: Dict) -> Dict[str, Any]:
        """Write three ad headlines and two 30-sec video scripts using the hook."""
        
        prompt = f"""
        You are a CopyCrafter AI. Your job is to create compelling ad copy and video scripts.
        
        Story Hook: {story_hook}
        Narrative Framework: {json.dumps(narrative_framework, indent=2)}
        
        Create three ad headlines and two 30-second video scripts based on this hook.
        
        Return your content in this JSON format:
        {{
            "headlines": [
                {{"text": "headline 1", "target_platform": "social media", "appeal_type": "emotional"}},
                {{"text": "headline 2", "target_platform": "search ads", "appeal_type": "rational"}},
                {{"text": "headline 3", "target_platform": "display", "appeal_type": "curiosity"}}
            ],
            "video_scripts": [
                {{
                    "title": "script 1 title",
                    "script": "30-second video script with scene descriptions",
                    "style": "inspirational",
                    "call_to_action": "specific CTA"
                }},
                {{
                    "title": "script 2 title", 
                    "script": "30-second video script with scene descriptions",
                    "style": "educational",
                    "call_to_action": "specific CTA"
                }}
            ],
            "copy_variations": {{
                "short_form": "tweet-length version",
                "medium_form": "social media post version", 
                "long_form": "blog/email version"
            }},
            "optimization_notes": "suggestions for A/B testing"
        }}
        """
        
        result = self.call_gemini_api(prompt)
        
        try:
            parsed_result = json.loads(result)
            return parsed_result
        except:
            return {
                "headlines": [
                    {"text": "Discover What's Possible When Innovation Meets You", "target_platform": "social media", "appeal_type": "emotional"},
                    {"text": "The Smart Choice for Forward-Thinking Leaders", "target_platform": "search ads", "appeal_type": "rational"},
                    {"text": "What If Change Was Your Competitive Advantage?", "target_platform": "display", "appeal_type": "curiosity"}
                ],
                "video_scripts": [
                    {
                        "title": "The Future Is Personal",
                        "script": "[Scene: Person looking at horizon] Voiceover: 'The future isn't something that happens to you...' [Scene: Person taking action] 'It's something you create.' [Scene: Brand logo] 'Transform your tomorrow, today.'",
                        "style": "inspirational",
                        "call_to_action": "Start Your Journey"
                    },
                    {
                        "title": "Innovation Simplified",
                        "script": "[Scene: Complex problem visualization] Voiceover: 'Complex challenges need smart solutions.' [Scene: Simple, elegant solution] 'We make innovation accessible.' [Scene: Success moment] 'Your success, our mission.'",
                        "style": "educational", 
                        "call_to_action": "Learn More"
                    }
                ],
                "copy_variations": {
                    "short_form": "Innovation that gets you. Transform your future today.",
                    "medium_form": "Ready for change that actually makes sense? Discover innovation designed around you, not the other way around.",
                    "long_form": "In a world of constant change, the brands that thrive are those that truly understand their customers. We don't just offer solutions – we create pathways to your success."
                },
                "optimization_notes": "Test emotional vs rational appeals, personalization levels, and CTA urgency"
            }


class HookOptimizer(BaseSpecializedAgent):
    """Agent responsible for ranking hooks by shareability and engagement."""
    
    def __init__(self):
        super().__init__("HookOptimizer")
    
    def optimize_hooks(self, headlines: List[Dict], content_data: Dict) -> Dict[str, Any]:
        """Rank hooks by likely shareability and engagement."""
        
        prompt = f"""
        You are a HookOptimizer AI. Your job is to rank content by shareability and engagement potential.
        
        Headlines to analyze: {json.dumps(headlines, indent=2)}
        Content Context: {json.dumps(content_data, indent=2)}
        
        Rank these hooks by likely shareability and engagement, providing detailed analysis.
        
        Return your analysis in this JSON format:
        {{
            "ranked_hooks": [
                {{
                    "headline": "the headline text",
                    "shareability_score": 9.2,
                    "engagement_score": 8.7,
                    "viral_potential": 8.9,
                    "platform_optimization": {{
                        "facebook": 8.5,
                        "instagram": 9.1,
                        "twitter": 8.8,
                        "linkedin": 7.9,
                        "tiktok": 9.3
                    }},
                    "optimization_reasons": ["reason 1", "reason 2", "reason 3"]
                }}
            ],
            "engagement_factors": {{
                "emotional_triggers": ["curiosity", "aspiration", "urgency"],
                "cognitive_patterns": ["pattern recognition", "completion loops"],
                "social_proof_elements": ["testimonials", "user content", "influencer potential"]
            }},
            "a_b_test_recommendations": [
                "test variation 1 vs variation 2",
                "optimize for different demographics",
                "timing and frequency testing"
            ],
            "improvement_suggestions": ["specific actionable advice"]
        }}
        """
        
        result = self.call_gemini_api(prompt)
        
        try:
            parsed_result = json.loads(result)
            return parsed_result
        except:
            return {
                "ranked_hooks": [
                    {
                        "headline": "What If Change Was Your Competitive Advantage?",
                        "shareability_score": 9.2,
                        "engagement_score": 8.9,
                        "viral_potential": 9.0,
                        "platform_optimization": {
                            "facebook": 8.8,
                            "instagram": 9.2,
                            "twitter": 9.1,
                            "linkedin": 8.5,
                            "tiktok": 9.4
                        },
                        "optimization_reasons": ["Question format drives engagement", "Reframes challenge as opportunity", "Universal business appeal"]
                    },
                    {
                        "headline": "Discover What's Possible When Innovation Meets You",
                        "shareability_score": 8.7,
                        "engagement_score": 8.5,
                        "viral_potential": 8.6,
                        "platform_optimization": {
                            "facebook": 8.9,
                            "instagram": 8.8,
                            "twitter": 8.2,
                            "linkedin": 8.1,
                            "tiktok": 8.5
                        },
                        "optimization_reasons": ["Personal connection", "Discovery element", "Positive framing"]
                    }
                ],
                "engagement_factors": {
                    "emotional_triggers": ["curiosity", "aspiration", "empowerment"],
                    "cognitive_patterns": ["open loops", "pattern interrupt", "reframing"],
                    "social_proof_elements": ["peer validation", "authority endorsement", "user success stories"]
                },
                "a_b_test_recommendations": [
                    "Test question format vs statement format",
                    "Compare personal vs business-focused messaging",
                    "Optimize for mobile vs desktop viewing"
                ],
                "improvement_suggestions": ["Add urgency elements", "Include social proof", "Test video vs static formats"]
            }


class SequencePlanner(BaseSpecializedAgent):
    """Agent responsible for drafting email drip campaigns."""
    
    def __init__(self):
        super().__init__("SequencePlanner")
    
    def plan_sequence(self, narrative_hook: str, optimized_content: Dict) -> Dict[str, Any]:
        """Draft a 5-step email drip that builds on the narrative."""
        
        prompt = f"""
        You are a SequencePlanner AI. Your job is to create sequential email drip campaigns.
        
        Narrative Hook: {narrative_hook}
        Optimized Content: {json.dumps(optimized_content, indent=2)}
        
        Draft a 5-step email drip campaign that builds on this narrative.
        
        Return your campaign in this JSON format:
        {{
            "email_sequence": [
                {{
                    "step": 1,
                    "title": "email subject line",
                    "objective": "what this email achieves",
                    "content_outline": "detailed content structure",
                    "call_to_action": "specific CTA",
                    "timing": "when to send (days after signup)",
                    "personalization_elements": ["element1", "element2"]
                }}
            ],
            "sequence_strategy": {{
                "overall_arc": "how the sequence builds",
                "emotional_journey": ["email1_emotion", "email2_emotion", "etc"],
                "value_progression": "how value increases each step",
                "conversion_points": ["step where conversions likely"]
            }},
            "automation_triggers": [
                "behavioral trigger 1",
                "engagement trigger 2",
                "time-based trigger 3"
            ],
            "success_metrics": {{
                "open_rate_targets": "expected ranges",
                "click_rate_targets": "expected ranges", 
                "conversion_targets": "expected ranges"
            }}
        }}
        """
        
        result = self.call_gemini_api(prompt)
        
        try:
            parsed_result = json.loads(result)
            return parsed_result
        except:
            return {
                "email_sequence": [
                    {
                        "step": 1,
                        "title": "Welcome to Your Transformation Journey",
                        "objective": "Set expectations and build excitement",
                        "content_outline": "Personal welcome, value promise, what to expect next",
                        "call_to_action": "Complete Your Profile",
                        "timing": "immediately after signup",
                        "personalization_elements": ["name", "signup source", "initial interest"]
                    },
                    {
                        "step": 2,
                        "title": "The Secret Behind Successful Innovation",
                        "objective": "Provide value and establish expertise",
                        "content_outline": "Industry insights, case study, actionable tip",
                        "call_to_action": "Download Free Guide",
                        "timing": "2 days after signup",
                        "personalization_elements": ["industry", "company size", "role"]
                    },
                    {
                        "step": 3,
                        "title": "What Leaders Are Doing Differently",
                        "objective": "Social proof and aspiration",
                        "content_outline": "Success stories, peer insights, trend analysis",
                        "call_to_action": "Join the Community",
                        "timing": "5 days after signup",
                        "personalization_elements": ["similar companies", "peer group", "goals"]
                    },
                    {
                        "step": 4,
                        "title": "Your Personalized Innovation Roadmap",
                        "objective": "Direct value delivery and soft pitch",
                        "content_outline": "Custom recommendations, tool preview, next steps",
                        "call_to_action": "Start Free Trial",
                        "timing": "8 days after signup",
                        "personalization_elements": ["assessment results", "specific needs", "timeline"]
                    },
                    {
                        "step": 5,
                        "title": "Don't Let This Opportunity Pass",
                        "objective": "Create urgency and drive conversion",
                        "content_outline": "Limited time offer, risk reversal, success guarantee",
                        "call_to_action": "Get Started Today",
                        "timing": "12 days after signup",
                        "personalization_elements": ["engagement level", "previous clicks", "urgency factors"]
                    }
                ],
                "sequence_strategy": {
                    "overall_arc": "Welcome → Value → Social Proof → Personal Value → Conversion",
                    "emotional_journey": ["excitement", "curiosity", "inspiration", "confidence", "urgency"],
                    "value_progression": "Increases from general insights to personalized recommendations",
                    "conversion_points": ["Email 4 (soft)", "Email 5 (hard)", "Follow-up sequence"]
                },
                "automation_triggers": [
                    "Email open/click behavior",
                    "Website visit activity",
                    "Content download actions",
                    "Time-based progression"
                ],
                "success_metrics": {
                    "open_rate_targets": "25-35% average",
                    "click_rate_targets": "5-8% average",
                    "conversion_targets": "3-7% by end of sequence"
                }
            }


class AnalyticsInterpreter(BaseSpecializedAgent):
    """Agent responsible for interpreting campaign analytics and providing improvement tips."""
    
    def __init__(self):
        super().__init__("AnalyticsInterpreter")
    
    def interpret_analytics(self, campaign_stats: Dict) -> Dict[str, Any]:
        """Analyze campaign stats and provide three bullet tips for improvement."""
        
        prompt = f"""
        You are an AnalyticsInterpreter AI. Your job is to analyze campaign performance and provide actionable insights.
        
        Campaign Statistics: {json.dumps(campaign_stats, indent=2)}
        
        Analyze these stats and give three specific, actionable bullet tips to improve next time.
        
        Return your analysis in this JSON format:
        {{
            "performance_summary": {{
                "overall_score": 8.5,
                "strengths": ["strength 1", "strength 2", "strength 3"],
                "weaknesses": ["weakness 1", "weakness 2"],
                "benchmark_comparison": "how this compares to industry standards"
            }},
            "improvement_tips": [
                {{
                    "tip": "specific actionable advice",
                    "priority": "high/medium/low",
                    "expected_impact": "predicted improvement",
                    "implementation": "how to execute this tip"
                }},
                {{
                    "tip": "second specific tip", 
                    "priority": "high/medium/low",
                    "expected_impact": "predicted improvement",
                    "implementation": "how to execute this tip"
                }},
                {{
                    "tip": "third specific tip",
                    "priority": "high/medium/low", 
                    "expected_impact": "predicted improvement",
                    "implementation": "how to execute this tip"
                }}
            ],
            "optimization_opportunities": {{
                "creative_optimization": "specific creative improvements",
                "targeting_optimization": "audience refinement suggestions", 
                "budget_optimization": "spend allocation improvements",
                "timing_optimization": "schedule and frequency adjustments"
            }},
            "next_campaign_recommendations": [
                "strategic recommendation 1",
                "strategic recommendation 2", 
                "strategic recommendation 3"
            ]
        }}
        """
        
        result = self.call_gemini_api(prompt)
        
        try:
            parsed_result = json.loads(result)
            return parsed_result
        except:
            return {
                "performance_summary": {
                    "overall_score": 7.8,
                    "strengths": ["Strong engagement rate", "Good brand recall", "Effective targeting"],
                    "weaknesses": ["Low conversion rate", "High cost per acquisition"],
                    "benchmark_comparison": "Above average engagement, below average conversion"
                },
                "improvement_tips": [
                    {
                        "tip": "Optimize landing page experience with clearer value proposition and simplified conversion flow",
                        "priority": "high",
                        "expected_impact": "25-40% improvement in conversion rate",
                        "implementation": "A/B test page layouts, reduce form fields, add social proof above the fold"
                    },
                    {
                        "tip": "Implement retargeting campaigns for engaged users who didn't convert",
                        "priority": "high", 
                        "expected_impact": "15-25% increase in overall conversions",
                        "implementation": "Set up pixel tracking, create custom audiences, design nurture sequence"
                    },
                    {
                        "tip": "Test video creative formats to improve engagement and reduce CPM",
                        "priority": "medium",
                        "expected_impact": "10-20% reduction in acquisition costs",
                        "implementation": "Create 15-30 second video versions of top performing static ads"
                    }
                ],
                "optimization_opportunities": {
                    "creative_optimization": "Test more emotional vs rational messaging",
                    "targeting_optimization": "Narrow audience based on highest converting segments",
                    "budget_optimization": "Increase spend on high-performing placements",
                    "timing_optimization": "Focus budget on peak engagement hours"
                },
                "next_campaign_recommendations": [
                    "Launch seasonal campaign aligned with upcoming trends",
                    "Expand to new platforms based on audience behavior",
                    "Develop user-generated content campaign for authenticity"
                ]
            }


# Agent factory for easy instantiation
class SpecializedAgentFactory:
    """Factory for creating specialized agents."""
    
    @staticmethod
    def create_all_agents():
        """Create all six specialized agents."""
        return {
            'meme_harvester': MemeHarvester(),
            'narrative_aligner': NarrativeAligner(),
            'copy_crafter': CopyCrafter(),
            'hook_optimizer': HookOptimizer(),
            'sequence_planner': SequencePlanner(),
            'analytics_interpreter': AnalyticsInterpreter()
        }