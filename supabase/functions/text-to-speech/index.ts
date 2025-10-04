import "jsr:@supabase/functions-js/edge-runtime.d.ts";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Client-Info, Apikey",
};

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response(null, {
      status: 200,
      headers: corsHeaders,
    });
  }

  try {
    const { text, language = 'en' } = await req.json();

    if (!text) {
      return new Response(
        JSON.stringify({ error: 'Text is required' }),
        {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        }
      );
    }

    const languageVoiceMap: Record<string, string> = {
      'en': 'en-US',
      'es': 'es-ES',
      'zh': 'zh-CN',
      'ar': 'ar-XA',
      'fr': 'fr-FR',
      'ru': 'ru-RU',
      'pt': 'pt-BR',
      'hi': 'hi-IN'
    };

    const voiceLocale = languageVoiceMap[language] || 'en-US';

    return new Response(
      JSON.stringify({
        message: 'Text-to-speech functionality will use browser Web Speech API',
        text: text,
        language: voiceLocale,
        audioUrl: null
      }),
      {
        headers: {
          ...corsHeaders,
          'Content-Type': 'application/json',
        },
      },
    );
  } catch (error) {
    console.error('Error:', error);
    return new Response(
      JSON.stringify({ error: error.message || 'Internal server error' }),
      {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      }
    );
  }
});